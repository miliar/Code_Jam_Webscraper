 
#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int _tmain(int argc, char* argv[])
{
	int cases;
	string name;
	int n;
	int length;
	int totalLength;
	int counterSubstr;

	cin >> cases;
	
	for(int i = 0; i < cases; i++)
	{
		cin >> name >> n;

		totalLength = name.length();
		length = name.length() - n + 1;
		counterSubstr = 0;
		for(int start = 0; start < length; start++)
		{
			for(int test = start, count = 0; test < totalLength; test++)
			{
				if(name[test] == 'a' || name[test] == 'e' || name[test] == 'i' || name[test] == 'o' || name[test] == 'u')
					count = 0;
				else
					count++;
				if(count == n)
				{
					counterSubstr += (totalLength - test);
					break;
				}
			}
		}
		
		cout << "Case #" << (i  + 1) <<  ": " << (counterSubstr) << endl;
	}

	return 0;
}
