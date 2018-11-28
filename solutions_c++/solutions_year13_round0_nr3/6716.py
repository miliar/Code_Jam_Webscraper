// GCJ Practice Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

bool isPalindrome( long double input )
{
	std::string number;
	std::stringstream strstream;
	strstream << input;
	strstream >> number;

	for ( int i = 0; i < (number.length()/2) ; i++ )
	{
		if ( number[i] != number[number.length() - (i + 1)] )
		{
			return false;
		}
	}
	return true;
}

vector<int> StrListToIntVector(string Input, char RightSeperator)//seperates a string of integers seperated by spaces into a vector of ints
{//right seperator is the symbol seperating the numbers. ie, ' ' or ','
	vector<int> IntList;
	string Sector;
	for ( int Active = 0 ; Active < Input.length() ; Active = ( Input.find( RightSeperator, Active+1  ) ) ) 
	{
		Sector = Input.substr( Active , Input.find(' ', Active+1 ) );
		IntList.push_back( atoi(Sector.c_str()) );
	}
	return IntList;
}

int main()
{
	ifstream InputFile;
	ofstream OutputFile;
	InputFile.open("C-small-attempt0.in");
	OutputFile.open("outtest.txt");
	if (!InputFile.is_open())
	{
		cout<< "file load failed.";
		cin.get();
		return 1;
	}
	string NumberOfCases;
	getline(InputFile, NumberOfCases);
	int Cases = atoi(NumberOfCases.c_str());

	vector<int> numbers;//Vector for data output
	string Line;
	
	for( int f = 0; f < Cases; f++ )
	{
		getline(InputFile, Line);
		numbers = StrListToIntVector(Line, ' ');
		int howMany = 0;
		//Process case values here
		for ( long double i = numbers[0]; i <= numbers[1]; i++ )
		{
			if ( isPalindrome(i) && isPalindrome(sqrt(i)) )
			{
				howMany++;
			}
		}
		//End process case values here
		OutputFile<<"Case #"<<f+1<<": "<<howMany<<endl;
		//Output code here
		
		//Output code ends

		numbers.clear();
	}
}

