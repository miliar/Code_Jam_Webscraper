// cppConsole.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string getLastWord(string input);
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	
	int T, S;
	string data;
	fin >> T;
	for (size_t i = 0; i < T; i++)
	{
		fin >> data;
		fout << "Case #" << (i + 1) << ": " << getLastWord(data) << endl;
	}
	return 0;
}

string getLastWord(string inputD){
	string s = "";
	s += inputD[0];
	for (size_t i = 1; i < inputD.length(); i++)
	{
		if (((int)inputD[i])<((int)s[0]))
		{
			s += inputD[i];
		}
		else{
			s = inputD[i] + s;
		}
	}
	return s;
}