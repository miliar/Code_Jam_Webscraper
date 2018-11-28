/*
 * codeJamCoutingSheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: BGH41158
 */

//#include "commonDefinition.h"

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string>     // std::string, std::stoi
#include <sstream>      // std::istringstream
#include <stack>
#include <queue>
#include <climits>
#include <list>
#include <fstream>
#include <string.h>
#include <sstream>
#include <algorithm>

using namespace std;

template <typename T>
string NumberToString ( T Number )
{
	ostringstream ss;
	ss << Number;
	return ss.str();
}




bool checkAllNumSeen(int numArr[], int size)
{

	for(int i = 0; i< size; i++)
	{
		if(numArr[i] != -1)
			return false;
	}
	return true;
}

unsigned long long countingSheep(unsigned long long  start)
{
	int numArr[] = {0,1,2,3,4,5,6,7,8,9};
	int size = 10;
	//unsigned long long  result = -1;
	if(start == 0)
		return -1;
	unsigned long long  N= 1;

	while(true)
	{
		unsigned long long  lastSeen  = start * N++;
		unsigned long long  product = lastSeen;
		if(product < 10)
		{
			numArr[product] = -1;
		}
		else
		{
			while(product >= 1)
			{
				int rem = product%10;
				numArr[rem] = -1;
				product = product/10;
			}
		}
		if(checkAllNumSeen(numArr,size))
			return lastSeen;
		//start = lastSeen;

	}
}

static void writeResult(ofstream& output,int testCase, string result)
{
	string prefix = "Case #";
	char buffer[1000];
	char *intStr = itoa(testCase, buffer, 10);
	prefix += string(intStr);
	prefix +=  ": ";
	result  = prefix + result;
	output<<result<<endl;
}

void testCountingSheep()
{
	try
	{
		ifstream inFile("A-large.in");

		int n = 0;
		if(inFile.is_open())
		{
			string line1;
			getline(inFile,line1);
			//cout<<"Line 1 is "<<line1<<endl;
			n = atoi(line1.c_str());
			cout<<"N is "<<n<<endl;
		}
		else
		{
			cout<<"Unable to open the file";
		}

		ofstream output("out",std::ios::out);
		int caseNum = 1;
		while(n-- >0)
		{
			string line;
			getline(inFile, line);
			unsigned long long  start = atoi(line.c_str());
			unsigned long long  result = countingSheep(start);
			string resultStr = "INSOMNIA";
			if(result != -1)
			{
				resultStr = NumberToString(result);

			}
			writeResult(output,caseNum++,resultStr);

		}
		output.close();
	}
	catch(const exception& e)
	{
		cout<<e.what();

	}

}


