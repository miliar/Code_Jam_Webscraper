#include<iostream>
#include<stdio.h>
#include <algorithm> 
#include <string>
#pragma warning(disable:4996)
using namespace std;

int War(double c_nao[1000], double c_ken[1000],int n)
{
	int i,j,point;
	point = 0;
	
	
	j = 0;
	for (i = 0; i < n; i++)
	{
		for (; j < n;j++)
		{
			if (c_nao[j] > c_ken[i])
			{
				point++;
				j++;
				break;
			}
		}
		
	}
	return point;
}
int War_D(double c_nao[1000], double c_ken[1000], int n)
{
	int i,j, point;
	double a, b;
	point = 0;
	j = 0;
	sort(c_ken, c_ken + n);
	sort(c_nao, c_nao + n);
    //reverse(c_nao, c_nao + n);
	for (i = 0; i < n; i++)
	{
		for (; j < n; j++)
		{
			if (c_nao[i] < c_ken[j])
			{

				point++;
				j++;
				break;
			}
		}

	}
	return point;
}
int main()
{
	//freopen("fun.in", "r", stdin);
	freopen("fun.out", "w", stdout);
	double c_nao[1000], c_ken[1000];
	int point_d, point;
	int i,j,t,n;
	
    cin >> t;
	for (i = 1; i <= t; i++)
	{
		
 		cin >> n;
		for (j = 0; j < n; j++)
			cin >> c_nao[j];
		for (j = 0; j < n; j++)
			cin >> c_ken[j];
		 //µßµ¹

		point = n - War_D(c_nao, c_ken, n);
		point_d = War(c_nao, c_ken, n);
		//memset(c_nao, 0, n);
		//memset(c_ken, 0, n);
		cout << "Case #" << i << ": " << point_d << " " << point << endl;
	}

	return 0;
}