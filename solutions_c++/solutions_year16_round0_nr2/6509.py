// GCJ2016_2.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//
#include <iostream>  // includes cin to read from stdin and cout to write to stdout

#include <sstream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

//#include "stdafx.h"


unsigned int length;
bool* bHappy;

bool Complete()
{	
	bool bRet = true;
	for (int i = 0; i < length; i++)
	{
		if (!bHappy[i])
		{
			bRet = false; 
			break;
		}
	}
	return bRet;
}

int ChangeSubset(int border)
{
	int ret = 0;
	for (int i = 0; i < border; i++)
	{
		bHappy[i] = !bHappy[i];
	}
	return ++ret;
}

int main()
{
	int t;
	std::string strIn;
	int out = 0;;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 0; i <= t; ++i) {
		getline(cin, strIn);  // read n and then m.
		if (i == 0) continue;
		length = strIn.length();
		bHappy = new bool[strIn.length()];
		for (int i = 0; i < strIn.length(); i++)
		{
			if(strIn.at(i) == '+')
			{ 
				bHappy[i] = true;
			}
			else
			{
				bHappy[i] = false;
			}
		}
		if (!Complete())
		{
			int outBefore = out;
			for (int i = 0; i < length - 1; i++)
			{
				if (bHappy[i] != bHappy[i + 1])
				{			
					out += ChangeSubset(i+1);
					i = -1;
				}
				
			}
			if (out == outBefore)
			{
				ChangeSubset(length);
				out++;
			}
		}
		else
		{
			out = 0;
		}

		if (!Complete())
		{
			ChangeSubset(length);
			++out;
		}
		delete bHappy;
		length = 0;		
		cout << "Case #" << i << ": " << out << endl;
		out = 0;

		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
    return 0;
}

