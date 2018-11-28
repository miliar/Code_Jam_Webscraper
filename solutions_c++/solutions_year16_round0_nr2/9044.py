/*
 * codeJamPancakes.cpp
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

const char MINUS = '-';
const char PLUS = '+';

template <typename T>
string NumberToString ( T Number )
{
	ostringstream ss;
	ss << Number;
	return ss.str();
}

void flipStack(stack<char>& ipStack)
{
	stack<char> tempStack;
	while(!ipStack.empty())
	{
		char t = ipStack.top();
		ipStack.pop();
		if( t == MINUS)
		{
			tempStack.push(PLUS);
		}
		else
		{
			tempStack.push(MINUS);
		}
	}
	ipStack = tempStack;
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

void printStack(stack<char> s, string str)
{
	cout<<str<<" is ";
	for(int i = 0; i < s.size(); i++)
	{
		cout<<" "<<s.top()<<" ";
	}
	cout<<endl;
}

int panCakesProblem(string& ipStr)
{
	int move = 0;
	int bottomBlankSide = -1;
	int topBlankSide = -1;
	if(ipStr[ipStr.size()-1] == MINUS)
		bottomBlankSide = ipStr.size();
	stack<char> ipStack;
	std::reverse(ipStr.begin(), ipStr.end());
	for(int i = 0; i< ipStr.size(); i++)
	{
		ipStack.push(ipStr[i]);
	}

	stack<char> auxStack;

	while(true)
	{
		while ( ! auxStack.empty() )
		{
			auxStack.pop();
		}

		int stackSize = ipStack.size();
		int i = 0;
		bottomBlankSide = -1;
		topBlankSide = 0;
		while(!ipStack.empty())
		{
			char t = ipStack.top();
			if(t == MINUS)
				bottomBlankSide = i;
			else
				topBlankSide++;
			ipStack.pop();
			i++;
			auxStack.push(t);

		}

		if(stackSize == topBlankSide)
			return move;
		if(bottomBlankSide == -1)
			return move;
		while( (stackSize - bottomBlankSide) > 1)
		{
			auxStack.pop();
			stackSize--;

		}
		if(!auxStack.empty())
		{
			flipStack(auxStack);
			move++;
			ipStack = auxStack;

		}



	}
	return move;

}



void testPancakes()
{
	try
	{
		ifstream inFile("B-large.in");

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

			int  result = panCakesProblem(line);
			string resultStr = NumberToString(result);

			writeResult(output,caseNum++,resultStr);

		}
		output.close();
	}
	catch(const exception& e)
	{
		cout<<e.what();

	}

}



