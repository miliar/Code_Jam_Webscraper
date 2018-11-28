// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

string solve(string inStr, int start)
{
	if(inStr.length() == 0)
		return string("");
		
	string* s = new string[10];
	
	s[0] = "ZERO";
	s[1] = "ONE";
	s[2] = "TWO";
	s[3] = "THREE";
	s[4] = "FOUR";
	s[5] = "FIVE";
	s[6] = "SIX";
	s[7] = "SEVEN";
	s[8] = "EIGHT";
	s[9] = "NINE";
	
	ostringstream res;
	
	string buffStr = "";
		
	int i = start;
			
	while(i < 10)
	{
		string goodStr = inStr;
		
		int success = 1;
		string first = "";
		
		for(int j = 0; j < s[i].length(); j++)
		{
			int added = 0;
			for(int k = 0; k < inStr.length(); k++)
			{
				// cout << inStr.length() << endl;
				
				if(inStr[k] != s[i][j] || added)
					buffStr += inStr[k];
				else
				{
					first += inStr[k];
					added = 1;
				}
			}
			inStr = buffStr;
			buffStr = "";
			
			if(!added)
				success = 0;
				
		}
		if(success)
		{
			for(int j = i; j < 10; j++)
			{
				string resStr = solve(inStr, j);
				
				if(resStr.compare(string("IMPOSSIBLE")) != 0)
				{
					res << i << resStr;
					return res.str();
				}	
			}
			i++;
			inStr = goodStr;
			// return string("IMPOSSIBLE");	
		
		}
		else
		{
			i++;
			inStr = goodStr;
		}
	}
	// cout << " " << inStr.length() << endl;
	return string("IMPOSSIBLE");
}


int main () {
	// define variables
	int numTC;

	ifstream myfile ("A-small-attempt3.in");
	ofstream savefile ("A-small-attempt3.out");
	
	if(!myfile.is_open())
		cout << "File not found";
	
	string* s = new string[10];
	
	s[0] = "ZERO";
	s[1] = "ONE";
	s[2] = "TWO";
	s[3] = "THREE";
	s[4] = "FOUR";
	s[5] = "FIVE";
	s[6] = "SIX";
	s[7] = "SEVEN";
	s[8] = "EIGHT";
	s[9] = "NINE";

	myfile >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		// savefile << "Case #" << (t + 1) << ": " << miss << endl;	
		// if(t != 73)
			// continue;
			
		
		string inStr;
		myfile >> inStr;
		
		savefile << "Case #" << (t + 1) << ": " << solve(inStr, 0) << endl;
	}

	myfile.close();
	savefile.close();

	return 0;
}


