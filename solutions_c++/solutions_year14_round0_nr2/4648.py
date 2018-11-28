#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

class Cookies
{
private:
	double C, F, X;

public:
	Cookies();
	void getInput(ifstream& file);
	double eval();
	void dumpOutput(ofstream& file, double minTime, int TCCnt);
};

Cookies::Cookies()
{
	C = F = X =0.0;
}

void Cookies::getInput(ifstream& file)
{
	file >> C;
	file >> F;
	file >> X;
}

void Cookies::dumpOutput(ofstream& file, double minTime, int TCCnt)
{
	std::stringstream ss1;
	ss1 << TCCnt+1;
	//std::string compMsg = "Case #"+ss1.str()+": "+msg+"\n";
	std::string compMsg = "Case #"+ss1.str()+": ";
	file.write(compMsg.c_str(), compMsg.length());
	//file << minTime;
	//file.write((const char*) &minTime, sizeof(minTime));
	std::stringstream ss;    
    ss.precision(std::numeric_limits<double>::digits10);//override the default
    ss << minTime;    
    file << ss.str(); //extract string from stream
	file << "\n";
}

double Cookies::eval()
{
	//double initC = 0.0;
	//double initF = 2.0;
	double minTime = 0;
	int valueOfn = -1;
	for(int i=0;i<10000000;i++)
	{
		double LH = X/(2+i*F);
		double RH = C/(2+i*F) + X/(2+(i+1)*F);
		if(LH < RH)
		{
			valueOfn = i;
			break;
		}
	}
	for(int i=0;i<valueOfn;i++)
	{
		minTime += C/(2+i*F);
	}
	minTime += X/(2+valueOfn*F);

	/*std::string msg;
	stringstream ss;
	ss << minTime;
	msg = ss.str();
	return msg;*/
	return minTime;
}

int main()
{
	ifstream file;
	file.open("input.in");
	ofstream fileOut;
	fileOut.open("output.out");
	std::string line;
	getline(file, line);
	//std::string outMsg;
	double minTime;
	int noOfTC = atoi(line.c_str());
	for(int i = 0; i < noOfTC; i++)
	{
		Cookies t;
		t.getInput(file);
		minTime = t.eval();
		t.dumpOutput(fileOut, minTime, i);
	}
	file.close();
	return 0;
}