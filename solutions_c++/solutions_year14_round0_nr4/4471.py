#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>
#include <vector>
#include <algorithm>

using namespace std;

class War
{
private:
	int N;
	//double NW[1000],KW[1000];
	std::vector<double> NW, KW;
	int wOut, dwOut;

public:
	War();
	void getInput(ifstream& file);
	void eval();
	void dumpOutput(ofstream& file, int TCCnt);

	void getWarOuput();
	void getDeceitWarOutput();
	double minMaxOf(double num,std::vector<double>& dupKW);
};

War::War()
{
	N = 0;
	/*for(int i = 0;i<1000;i++)
	{
		NW[i]= KW[i] = 0.0;
	}*/
	wOut = dwOut = 0;
}

void War::getInput(ifstream& file)
{
	file >> N;
	double temp;
	for(int i = 0;i<N;i++)
	{
		file >> temp;
		NW.push_back(temp);
	}
	for(int i = 0;i<N;i++)
	{
		file >> temp;
		KW.push_back(temp);
	}
}

void War::dumpOutput(ofstream& file, int TCCnt)
{
	std::stringstream ss1,ss2,ss3;
	ss1 << TCCnt+1;
	ss2 << wOut;
	ss3 << dwOut;
	std::string compMsg = "Case #"+ss1.str()+": "+ss3.str()+" " + ss2.str()+"\n";
	file.write(compMsg.c_str(), compMsg.length());
}

double War::minMaxOf(double num ,std::vector<double>& dupKW)
{
	double min = 10;
	for(std::vector<double>::iterator iter = dupKW.begin();
		iter!= dupKW.end(); iter++)
	{
		if(*iter > num && *iter < min)
			min = *iter;
	}
	return min;
}

void War::getWarOuput()
{
	std::vector<double> dupKW(KW);
	for(int i = 0;i< N;i++)
	{
		double minMax = minMaxOf(NW[i], dupKW);
		if(minMax == 10)
		{
			 minMax = *(std::min_element(dupKW.begin(), dupKW.end()));
			 wOut++;
		}
		std::vector<double>::iterator it = std::find(dupKW.begin(),dupKW.end(),minMax);
		dupKW.erase(it);
	}
}

void War::getDeceitWarOutput()
{
	std::vector<double> arr;
	for(int i=0;i<N;i++)
		arr.push_back(0);
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(NW[i] > KW[j])
				arr[i] = arr[i]+1;
		}
	}
	std::sort(arr.begin(),arr.end());
	for(int i=0;i<N;i++)
	{
		if(arr[i]==0)
			continue;
		if(arr[i]>dwOut)
			dwOut++;	
	}
}

void War::eval()
{	
	getWarOuput();
	getDeceitWarOutput();
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
		War t;
		t.getInput(file);
		t.eval();
		t.dumpOutput(fileOut, i);
	}
	file.close();
	return 0;
}