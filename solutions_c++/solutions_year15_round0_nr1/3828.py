#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int k, T;
	string s;
	long long int Smax, i;
	long long int Osum = 0;
	long long int toAdd = 0;
	cin >> T;
	int j;
	for (j = 1; j<=T; j++)
	{	
		cin >> Smax;
		Osum = 0;
		toAdd = 0;
		cin>>s;
		for (i = 0; i<=Smax; i++)
		{
			char ch = s[i];
			k = ch - '0';
			if (i!=0)
			{
				if (i > Osum + toAdd){
					toAdd = i - Osum;
				}
			}			
			Osum = Osum + k;
		}
		cout << "Case #" << j << ": " << toAdd << endl;
	}
	return 0;
}
