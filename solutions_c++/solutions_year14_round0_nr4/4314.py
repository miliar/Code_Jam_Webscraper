#include <fstream>
#include <cstdlib>
#include <iostream>
#include <math.h>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <string>
//#include <tr1/unordered_set.h>
//#include <tr1/hashtable.h>
//#include "Recursion.h"

using namespace std;

int War(vector<double>,vector<double>);
double KenChoice(vector<double>,double);
int deceitfulWar(vector<double>,vector<double>);
double secondMaximum(vector<double>);

int main() {

	ofstream result;
	result.open ("OutputProblemFour.txt");
	ifstream file;
	string lineBuffer;
	int numOfTestCases;
	int testCaseNum = 0;
	file.open("InputProblemFour.txt"); //
	getline(file,lineBuffer);
	numOfTestCases = atoi(lineBuffer.c_str());
	while (!file.eof()) {
		getline(file, lineBuffer);
		if (lineBuffer.length() == 0)
			continue; //ignore all empty lines
		else {
			testCaseNum++;
			//lineBuffer.erase(std::remove(lineBuffer.begin(), lineBuffer.end(), '\r'), lineBuffer.end());
			//lineBuffer.erase(std::remove(lineBuffer.begin(), lineBuffer.end(), ' '), lineBuffer.end());
			//std::replace(lineBuffer.begin(), lineBuffer.end(), ',', ' ');

			int deceitfulWarPoints = 0;
			int warPoints = 0;
			int N;
			vector<double> Naomi;
			vector<double> Ken;

			N = atoi(lineBuffer.c_str());

			getline(file,lineBuffer);
			std::istringstream buf(lineBuffer);
			std::istream_iterator<std::string> beg(buf), end;
			std::vector<std::string> tokens(beg, end);

			getline(file,lineBuffer);
			std::istringstream buf2(lineBuffer);
			std::istream_iterator<std::string> beg2(buf2), end2;
			std::vector<std::string> tokens2(beg2, end2);

			for(int i=0;i<N;i++)
			{
				Naomi.push_back(atof(tokens[i].c_str()));
				Ken.push_back(atof(tokens2[i].c_str()));
			}

			warPoints = War(Naomi,Ken);
			deceitfulWarPoints = deceitfulWar(Naomi,Ken);
			result << "Case #"<<testCaseNum<<": "<< deceitfulWarPoints<<" "<<warPoints<<"";
		}
		result << endl;
	}
	result.close();
	//getchar();
	return 0;
}

int War(vector<double> Naomi, vector<double> Ken)
{
	int points = 0;
	while(Naomi.size())
	{
		double chosen_Naomi = Naomi[0];
		Naomi.erase(std::remove(Naomi.begin(), Naomi.end(), chosen_Naomi), Naomi.end());
		double chosen_Ken = KenChoice(Ken,chosen_Naomi);
		Ken.erase(std::remove(Ken.begin(), Ken.end(), chosen_Ken), Ken.end());
		if(chosen_Naomi>chosen_Ken)
			points++;
	}
	return points;
}

double KenChoice(vector<double> Ken, double chosen_Naomi)
{
	double chosen_Ken = *(max_element(Ken.begin(), Ken.end()));
	if(chosen_Ken>chosen_Naomi)
	{
		for(int j=0;j<Ken.size();j++)
		{
			if (Ken[j]>chosen_Naomi && Ken[j]<chosen_Ken)
				chosen_Ken= Ken[j];
		}
	}
	else 
	{
		chosen_Ken=*(min_element(Ken.begin(), Ken.end()));
	}
	return chosen_Ken;
}

int deceitfulWar(vector<double> Naomi, vector<double> Ken)
{
	int points = 0;
	double chosen_Naomi,told_Naomi,chosen_Ken;

	while(Naomi.size())
	{
		double min_Naomi = *(min_element(Naomi.begin(), Naomi.end()));
		double min_Ken = *(min_element(Ken.begin(), Ken.end()));
		double max_Ken = *(max_element(Ken.begin(), Ken.end()));
		if (min_Naomi<min_Ken)
		{
			chosen_Naomi=min_Naomi;
			told_Naomi = secondMaximum(Ken)+0.000001;
		}
		else
		{
			chosen_Naomi = min_Naomi;
			told_Naomi = max_Ken+0.000001;
		}

		Naomi.erase(std::remove(Naomi.begin(), Naomi.end(), chosen_Naomi), Naomi.end());
		double chosen_Ken = KenChoice(Ken,told_Naomi);
		Ken.erase(std::remove(Ken.begin(), Ken.end(), chosen_Ken), Ken.end());
		if(chosen_Naomi>chosen_Ken)
			points++;
	}
	return points;
}

double secondMaximum(vector<double> vec)
{
	double max = *(max_element(vec.begin(),vec.end()));
	double secondMax = *(min_element(vec.begin(),vec.end()));
	for(int i=0;i<vec.size();i++)
	{
		if (vec[i]<max && vec[i]>secondMax)
			secondMax = vec[i];
	}
	return secondMax;
}