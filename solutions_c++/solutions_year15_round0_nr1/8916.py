#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<memory.h>
#include<queue>
#include<cmath>
#include<algorithm>
#include<stdio.h>
#include<stack>
#include<set>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t,smax,c=0,numofpeople=0,p;
	char ch;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		c = 0;
		numofpeople = 0;
		cin >> smax;
		for (int j = 0; j <= smax; ++j)
		{
			cin >> ch;
			p = ch - 48;
			if (p!=0 && j > numofpeople)
			{
				c = c + (j - numofpeople);
				numofpeople = numofpeople + (j - numofpeople);
			}
				
			numofpeople +=p;
		}
		cout << "Case #" << i << ": " << c << endl;
	}
	return 0;
}