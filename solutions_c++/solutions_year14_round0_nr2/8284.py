#include <iostream>
#include <string>
#include <sstream>
#include<fstream>

using namespace std;

std::string convert (double number){
    std::ostringstream buff;
	buff.precision(7);
    buff<<number;
	cout << buff.str() << endl;
    return buff.str();   
}

class TestCase
{
	double C;
	double F;
	double X;

	int totalFarm;
	double time;

public:
	std::string evaluate();
	void setValues(double c, double f, double x);
};

std::string TestCase::evaluate()
{
	totalFarm = 0;
	double temp;
	for(int i=1; ; i++)
	{
		temp = F*X - double(2)*C -double(i)*F*C;
		temp /= double(2)+double(i)*F;
		temp /= double(2)+(double(i)-1)*F;
		if(temp <= 0)break;
		totalFarm = i;
	}

	time = 0;
	for(int i=0; i<totalFarm; i++)
		time += C/(double(2)+double(i)*F);
	time += X/(double(2)+double(totalFarm)*F);

	char buffer[50];
	sprintf(buffer, "%lf", time);
	return string(buffer);
}

void TestCase::setValues(double c, double f, double x)
{
	C = c;
	F = f;
	X = x;
}

class Input
{
	int totalCase;
	TestCase *testCases;
	string result;

public:
	void init(string total);
	void setTestCase(int index, string str);
	void evaluate();
	string getResult();
	~Input();
};

Input::~Input()
{
	delete[] testCases;
}

string Input::getResult()
{
	return result;
}

void Input::evaluate()
{
	for(int i=0; i<totalCase; i++)
	{
		char buffer1[12];
		sprintf(buffer1, "Case #%d: ", i+1);
		result += string(buffer1) + testCases[i].evaluate() + string("\n");
	}
}

void Input::init(string temp)
{
	totalCase = atoi(temp.c_str());
	testCases = new TestCase[totalCase];
}

void Input::setTestCase(int index, string str)
{
	if(index >= totalCase)
		return;
	double c, f, x;
	sscanf(str.c_str(), "%lf %lf %lf", &c, &f, &x);
	testCases[index].setValues(c, f, x);
}

void main()
{
	Input input;
	std::string temp;
	ifstream infile;
	infile.open ("B-large.in");
        for(int i=0; !infile.eof(); i++) // To get you all the lines.
        {
	        getline(infile, temp); // Saves the line in STRING.
			if(i==0) input.init(temp);
			else
			{
				int caseIndex = i-1;
				input.setTestCase(i-1, temp);
			}
        }
	infile.close();

	input.evaluate();

	ofstream myfile;
	myfile.open ("output.txt");
	myfile << input.getResult();
	myfile.close();
}