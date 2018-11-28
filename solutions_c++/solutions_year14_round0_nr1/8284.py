#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class TestCase
{
	int arrangment[2][4][4];
	int answer[2];
	string result;

public:
	string evaluate();
	void assignAnswer(int ans, int index);
	void setArrangment(int index, int row, string str);
	friend ostream& operator<<(ostream& out, TestCase testCase);
};

string TestCase::evaluate()
{
	int count = 0;
	int soln = -1;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
			if(arrangment[0][answer[0]-1][i] == arrangment[1][answer[1]-1][j])
			{
				count++;
				soln = arrangment[0][answer[0]-1][i];
			}
	}
	char buffer[3];
	sprintf(buffer, "%d", soln);
	switch(count)
	{
	case 0:
		result = string("Volunteer cheated!");
		break;
	case 1:
		result = string(buffer);
		break;
	default:
		result = string("Bad magician!");
		break;
	}
	return result;
}

ostream& operator<<(ostream& out, TestCase testCase)
{
	for(int k=0; k<2; k++)
	{
		out << testCase.answer[k] << endl;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				out << testCase.arrangment[k][i][j] << " ";
			}
			out << endl;
		}
		out << endl;
	}
	out << endl;
	return out;
}

void TestCase::assignAnswer(int ans, int index)
{
	answer[index] = ans;
}

void TestCase::setArrangment(int setIndex, int row, string str)
{
	int index = str.find(' ');
	for(int i=0; index != -1; i++)
	{
		string temp = str.substr(0, index);
		str = str.substr(index+1, str.length()-index);
		index = str.find(' ');
		arrangment[setIndex][row][i] = atoi(temp.c_str());
	}
}

class Input
{
	int totalCase;
	string result;
public:
	TestCase *testCases;
	void init(string total);
	void evaluate();
	string getResult();
	~Input();
};

string Input::getResult()
{
	return result;
}

Input::~Input()
{
	delete[] testCases;
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

void main()
{
	Input input;
	string temp;
	ifstream infile;
	infile.open ("A-small-attempt1.in");
        for(int i=0; !infile.eof(); i++) // To get you all the lines.
        {
	        getline(infile, temp); // Saves the line in STRING.
			if(i==0) input.init(temp);
			else
			{
				int caseIndex = (i-1)/10;
				int setIndex = ((i-1)%10)/5;
				int rowIndex = (i-1)%5;
				if(rowIndex == 0)
					input.testCases[caseIndex].assignAnswer(atoi(temp.c_str()), setIndex);
				else
					input.testCases[caseIndex].setArrangment(setIndex, rowIndex-1, temp+" ");
			}
        }
	infile.close();

//	char buffer[] = "3\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n3\n1 2 5 4\n3 11 6 15\n9 10 7 12\n13 14 8 16\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n3\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n";
//	string str(buffer);
	input.evaluate();

	ofstream myfile;
	myfile.open ("output.txt");
	myfile << input.getResult();
	myfile.close();
}