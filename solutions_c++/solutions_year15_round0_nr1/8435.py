#include<iostream>
#include<cstdio>
#include<string>
#include<math.h>
#include<fstream>

using namespace std;

int t;
int s;
int y;
int n;
int sum = 0;
string sm;
string sj;


void main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	cin >> t;

	for(int i = 0; i < t; i++)
	{
		cin >> s;
		getline(cin,sm);
		y = 0;
		sum = 0;

		for(int j = 0; j <= s; j++)
		{
			sj = sm.substr(j+1,1);
			n = atoi(sj.c_str());

			if(j==0 && n ==0)
			{
				y++;
				sum = 1;
				continue;
			}

			if(n==0)
				continue;

			if(sum < j)
			{
				y = y + (j-sum);
				n = n + (j-sum);
			}
			sum = sum + n;
		}
		cout << "Case #" << i+1 << ": " << y << endl;
	}
}