// fair_square.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

ifstream input;
ofstream output;
int data; // data read from the file
int T; // number of test cases
int count;	// counter of number
int A, B;

void process(int min, int max);
bool ispalindrome(char *str);
bool issquare(int n);

int _tmain(int argc, _TCHAR* argv[])
{
	input.open(argv[1]);
	output.open("output.txt");

	if(input.is_open())
	{
		// get the number of test cases
		input >> data;
		T = data;
				
		// loop
		for(int i=0; i<T; i++)
		{
			cout << "Case #" << i+1 << ": ";
			output << "Case #" << i+1 << ": ";

			input >> data;
			A = data;
			input >> data;
			B = data;
			
			process(A, B);
		}
	}
	
	input.close();
	output.close();
	
	return 0;
}


void process(int min, int max)
{
	count = 0;
			
	for(int number = min; number <= max; number++)
	{
		char s[256];
		char ss[256];
		itoa(number, s, 10);
		
		if(ispalindrome(s))
		{
			if(issquare(number))
			{
				double sq_number = sqrt((double)number);
				int i_sq_number = sq_number;
				itoa(i_sq_number, ss, 10);
				if(ispalindrome(ss))
				{
					count++;
				}
			}
		}
	}
	
	cout << count << endl;
	output << count << endl;
}

bool ispalindrome(char *str)
{
	int i,j;

	for(i = 0,j =(strlen(str)-1); i<(strlen(str)/2);i++,j--)
	{
		if((str[i] )!= (str[j]))
		{
			return false;
		}
	}
	
	return true;
}

bool issquare(int n)
{
	double d_sqrt = sqrt( (double) n );
	//cout  << d_sqrt << endl;
	
	int i_sqrt = d_sqrt;
	//cout << i_sqrt << endl;
	
	if ( ( d_sqrt - i_sqrt ) < 0.0001 )
		return true;
	else
		return false;
}
