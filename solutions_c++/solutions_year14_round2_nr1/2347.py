#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>
#include <vector>
#include <set>
#include <iterator>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

class R1P1
{
private:
	int N;
	vector<string> Iarr;
	int out1;
public:
	R1P1();
	void getInput(ifstream& file);
	void eval();
	void dumpOutput(ofstream& file, int TCCnt);
	void compare();
};

R1P1::R1P1()
{
	N=0;	
	out1 = -1;
}

void R1P1::getInput(ifstream& file)
{
	file >> N;
	string temp;
	for(int i = 0;i<N;i++)
	{
		file >> temp;
		Iarr.push_back(temp);
	}
}

void R1P1::dumpOutput(ofstream& file, int TCCnt)
{
	std::stringstream ss1,ss2;
	ss1 << TCCnt+1;
	std::string compMsg = "Case #"+ss1.str()+": ";
	file.write(compMsg.c_str(), compMsg.length());
	if(out1 ==-1)
		ss2 <<"Fegla Won";
	else
		ss2 << out1;
	file << ss2.str() << "\n";
}

void R1P1::compare()
{
	int i,j,k,count1=0,count2=0,result=0;
	for(i=0,j=0;i<Iarr[0].length()&&j<Iarr[1].length();)
	{
		if(Iarr[0][i] == Iarr[1][j])
		{
			for(k=j;k<Iarr[1].length();k++)
			{
				if(Iarr[1][j] == Iarr[1][k])
					count1++;
				else
					break;
			}
			for(k=i;k<Iarr[0].length();k++)
			{
				if(Iarr[0][i] == Iarr[0][k])
					count2++;
				else
					break;
			}
			if(count1==count2)
			{
				i+=count1;
				j+=count1;
			}
			else if(count1<count2)
			{
				result += count2-count1;
				i+=count2;
				j+=count1;
			}
			else if(count1>count2)
			{
				result += count1-count2;
				i+=count2;
				j+=count1;
			}
			count1 = count2 = 0;

		}
		else 
		{
			return;
		}

	}
	if(i == Iarr[0].length() && j == Iarr[1].length())
		out1 = result;
}

void R1P1::eval()
{
	compare();
}

int main()
{
	ifstream file;
	file.open("input.in");
	ofstream fileOut;
	fileOut.open("output.out");
	std::string line;
	getline(file, line);
	int noOfTC = atoi(line.c_str());
	for(int i = 0; i < noOfTC; i++)
	{
		R1P1 t;
		t.getInput(file);
		t.eval();
		t.dumpOutput(fileOut, i);
	}
	file.close();
	return 0;
}