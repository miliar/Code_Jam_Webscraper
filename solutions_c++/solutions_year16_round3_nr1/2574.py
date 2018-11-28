#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
int al[100][100], an[100][100], r, c, m;
long long no;
int co[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
bool ch = false,ch1=true;
int max1, max2;
void max(int p[],int n)
{
	ch = false;
	int m1=0, m2=0,mp1,mp2;
	if (p[0] >= p[1])
	{
		m1 = p[0];
		m2 = p[1];
		mp1 = 0;
		mp2 = 1;
	}
	else
	{
		m1 = p[1];
		m2 = p[0];
		mp1 = 1;
		mp2 = 0;
	}
	int c1=0, c0=0,c2=0;
	if (p[0] == 0)
		c0++;
	if (p[0] == 1)
		c1++; 
	if (p[1] == 0)
		c0++; 
	if (p[1] == 1)
		c1++;
	if (p[0] == 2)
		c2++;
	if (p[1] == 2)
		c2++;
	for (int j = 2; j < n; j++)
	{
		if (p[j] == 0)
		{
			c0++;
		}
		/*else if (p[j] == 1)
		{
			c1++;
		}
		else if (p[j] == 2)
		{
			c2++;
		}*/
		if (m1 < p[j])
		{
			m2 = m1;
			mp2 = mp1;
			m1 = p[j];
			mp1 = j;
		}
		else if (m2 < p[j])
		{
			m2 = p[j];
			mp2 = j;
		}
	}
	/*if (c2 == 2 && c0 == (n-2))
	{
		 ch = true;
	}
	if (c1 == 2 && c0 == (n-2))
	{
		ch = true;
	}*/
	if (c0==n)
	{
		ch1 = false;
	}
	if (m1 == m2 && c0 == (n - 2))
	{
		ch = true;
	}
	max1 = mp1;
	max2 = mp2;
}
void main()
{
	long long t, n, p, i,temp;
	long long k;
	char c;
	
	int s[27];
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
		fin >> t;
	
	for (i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ": ";
		fin >> n;
		for (int j = 0; j < n; j++)
		{
			fin >> s[j];
		}
		no = 0;
		while (ch1)
		{
			max(s, n);
			if (ch1)
			{
				if (ch)
				{
					no += 2;
					fout << char(65+max1) << char(65+max2);
					s[max1]--;
					s[max2]--;
				}
				else
				{
					no += 1;
					fout << char(65+max1);
					s[max1]--;
				}
				fout << " ";
			}
		}
		fout<<"\n";
		ch1 = true;
		}
	fin.close();
	fout.close();
	}
