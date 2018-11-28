// GoogleCodejam_2013_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int p = 0; p < t; p++)
	{
		int s[101][101];
		int n,m;
		cin>>n>>m;

		int MAXr[100] ={0} , MAXc[100] = {0}; // max of row and  cul

		for (int j = 0; j < n; j++)
		{
			for (int k= 0; k < m; k++)
			{
				cin>>s[j][k];
				if(s[j][k] > MAXr[k])
					MAXr[k] = s[j][k];

				if(s[j][k] > MAXc[j])
					MAXc[j] = s[j][k];
			}
			
		}

		bool b[100][100];
		for (int i = 0; i < 100; i++)
		{
			for (int j = 0; j < 100; j++)
			{
				b[i][j] = false;
			}
		}
		

		// for Rows
		for (int i = 0; i < n; i++)
		{
			int max = 1, min= 100;
			for (int j= 0; j < m; j++)
			{
				if(s[i][j] > max)
					max =  s[i][j];
				if(s[i][j] < min)
					min = s[i][j];
			}
			if(max == min)
			{
				for (int k = 0; k < m; k++)
				{
					b[i][k] = true;
				}
			}
		}

		//for columns
		for (int i = 0; i < m; i++)
		{
			int max = 1, min= 100;
			for (int j= 0; j < n; j++)
			{
				if(s[j][i] > max)
					max =  s[j][i];
				if(s[j][i] < min)
					min = s[j][i];
			}
			if(max == min)
			{
				for (int k = 0; k < n; k++)
				{
					b[k][i] = true;
				}
			}
		}


		bool yes = true;
		for (int i = 0; i < n && yes; i++)
		{
			for (int j = 0; j < m && yes; j++)
			{


				if(b[i][j] == false && s[i][j] != MAXc[i] && s[i][j] !=MAXr[j] )
					yes = false;
			}
		}

		cout<<"Case #"<<p+1;
		if(yes)
			cout<<": YES\n";
		else
			cout<<": NO\n";
	}
	return 0;
}

