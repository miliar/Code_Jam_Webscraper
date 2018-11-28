#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int testCases;
	long changes;
	char c = '-', tempChar;
	cin >> testCases;
	for (int tc=0; tc < testCases; tc++) 
	{
		string s;
		cin >> s;
		changes = 0;
		int it1;
		for(it1=0; it1 < s.length(); it1++)
		{
			if(it1==0)
			{
				tempChar = s[0];
			}
			else
			{
				if(s[it1] != tempChar)
				{
					changes++;
					tempChar = s[it1];
				}
			}
		}
		if(s[it1-1] == c)
			changes++;
		cout << "Case #" << tc+1 << ": " << changes << endl;
	}
	return 0;
}
