// GCJ2016_1.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool bDigit[10] = { false,false,false,false,false,false,false,false,false,false };
void Reset()
{
	for (int i = 0; i < 10; i++)
	{
		bDigit[i] = 0;
	}
}
bool bComplete()
{
	bool bRet = true;
	for (int i = 0; i < 10; i++)
	{
		if(!bDigit[i])
		{ 
			bRet = false;
		}
	}
	return bRet;
}


int calcSteps(int in, int mod)
{
	int out = 0;
	if (in / 10 * mod > 0)
	{
		bDigit[in % 10] = true;
		out = calcSteps(in / 10, ++mod);
	}
	else
	{
		bDigit[in] = true;
		out++;
	}
	return out;
}

int main()
{
	int t, n;
	int out = 0;
	int mod = 1;
	int in = 1; 
	int it = 0;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		if(n != 0)
		{
			in = n;
			while(!bComplete())
			{
				out += calcSteps(in, mod);
				it++;
				in = n* (it+1);
				mod = 1;
				
			}
			
			cout << "Case #" << i << ": " << n*(it) << endl;
			out = 0;
			it = 0;
		}
		else
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		Reset();
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

