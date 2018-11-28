/* 
* File:   main.cpp
* Author: aa
*
* Created on February 4, 2014, 7:55 PM
*/

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

//using namespace std::tr1;
using namespace std;

int numOfSubSetsSumsToZero = 0;
void generateAllSubsetsOfSizeN(vector<int>, vector<int>, int );

int main(int argc, char** argv) {

	ofstream result;
	result.open ("OutputProblemOne.txt");
	ifstream file;
	string lineBuffer;
	int numOfTestCases;
	int testCaseNum = 0;
	file.open("InputProblemOne.txt"); //
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

			int volAns1 = atoi(lineBuffer.c_str());
			volAns1--;
			int** firstArrang;
			firstArrang = new int*[4];
			for(int i =0 ; i < 4; i++)
			{
				firstArrang[i] = new int[4];
				getline(file, lineBuffer);	
				std::istringstream buf(lineBuffer);
				std::istream_iterator<std::string> beg(buf), end;
				std::vector<std::string> tokens(beg, end);
				for (int j = 0; j < tokens.size(); j++)
					firstArrang[i][j]=(atoi(tokens[j].c_str()));
			}
			getline(file, lineBuffer);	
			int volAns2 = atoi(lineBuffer.c_str());
			volAns2--;
			int** secondArrang;
			secondArrang = new int*[4];
			for(int i =0 ; i < 4; i++)
			{
				secondArrang[i] = new int[4];
				getline(file, lineBuffer);	
				std::istringstream buf(lineBuffer);
				std::istream_iterator<std::string> beg(buf), end;
				std::vector<std::string> tokens(beg, end);
				for (int j = 0; j < tokens.size(); j++)
					secondArrang[i][j]=(atoi(tokens[j].c_str()));
			}

			int numOfInCommonCards = 0;
			int cardSolution = -1;

			for(int i = 0; i < 4; i++)
			{
				for(int j =0 ; j < 4 ; j++)
				{
					if(firstArrang[volAns1][i] == secondArrang[volAns2][j])
					{
						numOfInCommonCards++;
						cardSolution = firstArrang[volAns1][i];
					}
				}
			}

			if(numOfInCommonCards == 0)
				result << "Case #"<<testCaseNum<<": Volunteer cheated!";
			else if(numOfInCommonCards == 1)
				result << "Case #"<<testCaseNum<<": " << cardSolution;
			else if(numOfInCommonCards > 1)
				result << "Case #"<<testCaseNum<<": Bad magician!";
		}
		result << endl;
	}
	result.close();
	//getchar();
	return 0;
}
