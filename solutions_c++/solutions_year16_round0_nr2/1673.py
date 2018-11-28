// reading a text file
#include <iostream>
// #include <fstream>
// #include <sstream>
#include <string>
// #include <algorithm>
// #include <vector>
#include <cmath>
// #include <climits>

using namespace std;

int main () {
	// define variables
	int numTC;
	string p;

	// ifstream myfile ("sample-2-2016.in");
	// ofstream savefile ("sample-2-2016.out");
	
	// if(!myfile.is_open())
		// cout << "File not found";

	cin >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		cin >> p;
		
		int len = p.length();
		
		int start;
		int numFlip = 0;
		
		while(1)
		{
			// count +
			start = 0;
			while(start < len)
			{
				if(p[start] == '-')
					break;
				start++;
			}
			if(start == len)
			{
				cout << "Case #" << (t + 1) << ": " << numFlip << endl;
				break;
			}
			else if(start > 0) // flip
			{
				for(int i = 0; i < (start + 1)/2; i++)
				{
					char tmp = p[i];
					if(p[i] == '+')
						p[start-1-i] = '-';
					else
						p[start-1-i] = '+';
						
					if(tmp == '+')
						p[i] = '-';
					else
						p[i] = '+';
				}
				numFlip++;
			}
			
			// count - and flip
			start = 0;
			while(start < len) // count
			{
				if(p[start] == '+')
					break;
				start++;
			}
			// if(start == len)
				// start--;
			if(start > 0)// flip
			{
				for(int i = 0; i < (start + 1)/2; i++)
				{
					char tmp = p[i];
					if(p[i] == '+')
						p[start-1-i] = '-';
					else
						p[start-1-i] = '+';
						
					if(tmp == '+')
						p[i] = '-';
					else
						p[i] = '+';
				}
				numFlip++;
			}
		}
	}

	// myfile.close();
	// savefile.close();

	return 0;
}


