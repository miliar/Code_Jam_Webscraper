#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <fstream>
using namespace std;

int main() {
	int T, S, needed = 0, count = 0, caseX = 1;
	string s;
	ifstream myfile ("example.txt");
	if (myfile.is_open())
	{		
		myfile >> T;
		// cout << T << endl;

		while(T--)
		{
			needed = count = 0;
			myfile >> S >> s;
			// cout << S << " ";

			count = s[0] - '0';

			for (int i = 1; i <= S; ++i)
			{
				int num = s[i] - '0';
				if(num)
				{
					if(i > count)
					{
						int dif = i - count;
						// if(dif > needed) needed = dif;
						needed += dif;
						count += dif;
					}
					count += num;					
				}							
			}
			cout << "Case #" << caseX++ << ": " << needed << endl; 			
		}

		myfile.close();
	}

	else cout << "Unable to open file"; 
    return 0;
}
