#include<iostream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<string.h>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
	int test, sMax, s[1005], frnds, temp_1;
	char temp[1005];
	cin>> test;
	for(int i=0;i < test;i++)
	{
		cin>> sMax;
		temp_1 = frnds = 0;
		for(int j=0;j <= sMax;j++)
		{
			cin>> temp[j];
			s[j] = temp[j] - '0';
			if (temp_1 < j && s[j] != 0)
			{
				frnds += j-temp_1;
				temp_1 += frnds;
			}
			temp_1 += s[j];
		}
		cout<< "Case #" << i+1 << ": " << frnds << endl; 
	}
}