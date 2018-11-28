#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
using namespace std;
int al[100][100], an[100][100], r, c, m;
double no;
int co[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
bool ch = false;
void check()
{
	ch = true;
	for (int x = 0; x < 10; x++)
	{
		if (co[x] == 0)
			ch = false;
	}
}
void main()
{
	int t, n, p, s, j=1, i,temp;
	double k;
	int co1[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (i = 1; i <= t; i++)
	{
		fin >> no;
		fout << "Case #" << i << ": ";
		if (no == 0)
			fout << "INSOMNIA\n";
		else
		{
			k = no;
			while (!ch)
			{
				temp = k;
				while (temp != 0)
				{
					s=temp % 10;
					co[s] = 1;
					temp = temp / 10;
				}
				check();
				j++;
				k = no*j;
			}
			
			fout << k/j*(j-1) <<"\n";
			j = 0;
			ch = false;
			for (int x = 0; x < 10; x++)
			{
				co[x] = 0;
			}
		}
	}
}
