#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

class Magic
{
private:
	int firstArr[4][4];
	int secondArr[4][4];
	int firstAns,secondAns;

public:
	Magic();
	void getInput(ifstream& file);
	std::string eval();
	void dumpOutput(ofstream& file, std::string outMsg, int TCCnt);
};

Magic::Magic()
{
	firstAns = secondAns = 0;
	for(int i =0;i<4;i++)
	{
		for(int j =0;j<4;j++)
		{
			firstArr[i][j] = 0;
			secondArr[i][j] = 0;
		}
	}
}

void Magic::getInput(ifstream& file)
{
	file >> firstAns;	
	for(int i =0;i<4;i++)
	{
		for(int j =0;j<4;j++)
		{
			file >> firstArr[i][j];
		}
	}
	file >> secondAns;	
	for(int i =0;i<4;i++)
	{
		for(int j =0;j<4;j++)
		{
			file >> secondArr[i][j];
		}
	}
}

void Magic::dumpOutput(ofstream& file, std::string msg, int TCCnt)
{
	std::stringstream ss1;
	ss1 << TCCnt+1;
	std::string compMsg = "Case #"+ss1.str()+": "+msg+"\n";
	file.write(compMsg.c_str(), compMsg.length());
}

std::string Magic::eval()
{
	int commonElemCnt = 0,commonElem;
	int k1,k2;
	for(k1=0;k1<4;k1++)
	{
		for(k2=0;k2<4;k2++)
		{
			if(firstArr[firstAns-1][k1] == secondArr[secondAns-1][k2] )
			{
				commonElemCnt++;
				commonElem = firstArr[firstAns-1][k1];
			}
		}
	}
	std::string msg;
	if(commonElemCnt == 1)
	{
		std::stringstream ss;
		ss << commonElem;
		msg =ss.str();	
	}
	else if (commonElemCnt == 0)
		msg = "Volunteer cheated!";
	else if(commonElemCnt > 1)
		msg = "Bad magician!";
	return msg;
}

int main()
{
	ifstream file;
	file.open("input.in");
	ofstream fileOut;
	fileOut.open("output.out");
	std::string line;
	getline(file, line);
	std::string outMsg;
	int noOfTC = atoi(line.c_str());
	for(int i = 0; i < noOfTC; i++)
	{
		Magic t;
		t.getInput(file);
		outMsg = t.eval();
		t.dumpOutput(fileOut, outMsg, i);
	}
	file.close();
	return 0;
}