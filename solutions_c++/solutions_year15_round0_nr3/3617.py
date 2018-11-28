// GCJ_3.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#pragma warning (disable : 4996)


typedef long long nil;

int mul(int a, int b)
{
	if (a == 1)
		return b;
	if (b == 1)
		return a;
	if (a == b)
		return -1;
	if (a == 2 && b == 3)
		return 4;
	if (a == 2 && b == 4)
		return -3;
	if (a == 3 && b == 2)
		return -4;
	if (a == 3 && b == 4)
		return 2;
	if (a == 4 && b == 2)
		return 3;
	if (a == 4 && b == 3)
		return -2;
}

int nu(char ch)
{
	if (ch == 'i')
	{
		return 2;
	}
	if (ch == 'j')
	{
		return 3;
	}
	if (ch == 'k')
	{
		return 4;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, bk;
	cin >> t;
	for (bk = 1; bk <= t; bk++)
	{
		nil l, x, i, j, k, temp, mi = 0, ni=2;
		char ch[100000];
		cin >> l >> x;
		cin.clear();
		for (i = 0; i < l; i++)
		{
			cin >> ch[i];
		}
		
		if (l == 1)
			goto end;
		/*for (i = 1; i < x; i++)
		{
			for (j = 0; j < l; j++)
			{
				ch[l*i + j] = ch[j];
			}
		}
		l = l*x;*/
		for (i = 0; i < l*x; i++)
		{
			//cout << "start i:" << i << "   and: " << nu(ch[i%l]) << endl;
			temp = nu(ch[i%l]);

			mi = 0;
			while (!(temp == ni && mi % 2 == 0))
			{
				
				temp = mul(temp, nu(ch[(i + 1)%l]));
				///cout << "i:" << i << "  temp:" << temp << "   " << nu(ch[i%l]) << "  2nd:" << nu(ch[(i + 1)%l]) << endl;
				if (temp < 0)
				{
					temp = -temp;
					mi++;
				}
				i++;
				if (i >= l*x)
					goto end;
			}
			//cout << "done" << endl;
			ni++;
			//i++;
			if (ni == 4)
				break;
		}
		//cout << "start   i:" << i << endl;
		temp = nu(ch[(i + 1)%l]);
		mi = 0;
		//cout << "start   temp:" << temp << endl;
		//cout << "started " << endl;
		for (j = i+1; j < l*x-1; j++)
		{
			//cout << "Numner:" << ch[j%l] << endl;
			temp = mul(temp, nu(ch[(j + 1)%l]));
			if (temp < 0)
			{
				temp = -temp;
				mi++;
			}
			//cout << "Temp:" << temp  << "  j:" << j << endl;
		}
		//cout << "start temp:" << temp << endl;
		if (temp == 4 && ni == 4 && mi%2==0)
		{
			cout << "Case #" << bk << ": YES";
		}
		else
		{
			end:
			cout << "Case #" << bk << ": NO";
		}
		cout << endl;
	}
	return 0;
}