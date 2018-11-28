#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
	int k, t;
	long long int Smax, i;
	long long int st = 0;
	long long int pr = 0;
	string s;
	cin >> t;
	for (int j = 1; j<=t; j++)
	{	
		cin >> Smax;
		st = 0;
		pr = 0;
		cin>>s;
		for (i = 0; i<=Smax; i++)
		{
			char ch = s[i];
			k = ch - '0';
			if (i!=0)
			{
				if (i > st + pr)
					pr = i - st;
			}			
			st+=k;
		}
		cout << "Case #" << j << ": " << pr << endl;
	}
	return 0;
}
