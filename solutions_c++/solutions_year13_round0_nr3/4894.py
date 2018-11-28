
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "math.h"
using namespace std;

bool square(long long a)
{
	long double ld =sqrt((long double)a);
	if (abs(ld - floor(ld)) > 1e-10)
	{
		return false;
	}
	return true;
}
bool palindrome(long long a)
{
	stringstream strm;
	strm << a;
	string str;
	strm >> str;
	int lg=int(str.size());
	int mid=lg/2;
	lg--;
	bool result=true;
	for(int i=0; i<mid; i++,lg--)
	{
		if(str[i]!=str[lg])
		{
			result=false;
			break;
		}
	}
	return result;
}

bool fairandsquare(long long a)
{
	long double ld =sqrt((long double)a);
	if (abs(ld - floor(ld)) > 1e-10)
	{
		return false;
	}
	else
	{
		return palindrome((long long) ld);
	}
}

int main(void)
{
	ifstream infile("d:\\C-small-attempt0.in");
	ofstream outfile("d:\\o.out");
	int nDataCount;
	infile >> nDataCount;
	int k;
	long long num;
	for (k = 0; k < nDataCount; k++)
	{
		long long lbegin, lend;
		infile >> lbegin >> lend;
		num = 0;
		for (long long i = lbegin; i <=lend; i++)
		{
			long double ld =sqrt((long double)i);
			if (abs(ld - floor(ld)) > 1e-10)
			{
				continue;
			} 
			else if (palindrome(i) == false)
			{
				continue;
			} 
			else if (fairandsquare(i) == false)
			{
				continue;
			}				
			num ++;
		}
		outfile << "Case #"<<k+1<<": "<< num <<endl;
	}
	return 0;
}

