#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main ()
{
	int T, nvalue, namelength, start, ilimit, length, countcons, ans;
	int testCase, i, j;
	bool isNvalued;
	char ch;
	string name, str;
	
	ifstream ifs ("input.in");
	ofstream ofs ("output.txt");
	
	ifs >> T;
	
	for (testCase=1; testCase<=T; testCase++)
	{
		//Read data
		ifs >> name >> nvalue;
		
		//Find solution
		ans=0;
		namelength = name.length();
		for (start=0; start<namelength; start++)
		{
			isNvalued = false;
			countcons=0;
			str.clear();
			for (i=start; i<namelength; i++)
			{
				if (isNvalued)
				{
					ans++;
				}
				else //not nValued
				{
					str.push_back(name[i]);
					length = str.length();
					countcons=0;
					for (j=0; j<length && !isNvalued; j++)
					{
						
						ch = str[j];
						if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
						{
							countcons = 0;
						}
						else //is cons
						{
							countcons++;
							if (countcons >= nvalue)
							{
								isNvalued = true;
								ans++;
							}
						}
					}
				}
			}
		}
			
		//Output
		ofs << "Case #"  << testCase << ": " << ans << endl;
	}
}
