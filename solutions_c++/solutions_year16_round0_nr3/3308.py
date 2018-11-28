#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
long long l=10, d, n, t, len,v;
long long a[9], b[100], o;
bool ch=true;
long long checkprime()
{
	/*for (long long x = 2; x < v / 2; x++)
	{
		if (v%x == 0)
			return x;
	}
	ch = false;
	return 0;*/
	if (v == 2) {
		ch = false;
		return 0;
	}
			if( v == 3 )
			{
				ch = false;
				return 0;
				
			}
			if (v % 2 == 0)
				return 2;
			if (v % 3 == 0)
				return 3;

			long long i = 5;
			long long w = 2;

			while (i * i <= v)
			{
				if (v % i == 0)
					return i;

				i += w;
					w = 6 - w;
			}
			ch = false;
			return 0;
}
void check()
{
	long long temp,cou=0;
	for (int x = 2; x <= 10; x++)
	{
		temp = d;
		v = 0;
		cou = 0;
		while (temp != 0)
		{
			v = v + (temp % 10) * pow(x, cou);
			cou++;
			temp = temp / 10;
		}
		a[x-2]=checkprime();
		if (!ch)
			x = 10;
	}
}

void main()
{
	long long t, p, s, j, i, c;
	long long k;
	int count = 0;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (i = 1; i <= 1; i++)
	{
		fout << "Case #" << i << ": \n";
		fin >> n >> j;
		long long temp;
		b[0] = 1;
		b[n - 1] = 1;
		for (s = 0; s < pow(2,n-2); s++)
		{
			temp = s;
			for (p = 1; p < n-1; p++)
			{
				b[p] = 0;
			}
			c = 0;
			while (temp != 0)
			{
				b[n-c-2] = temp % 2;
				temp = temp / 2;
				c++;
			}
			d = 0;
			for ( int y = 0; y < n;y++)
			{
				d = d * l + b[y];
				//cout << d<<"k";
			}
			check();
			if (ch)
			{
				fout << d;
				for (int x = 0; x < 9; x++)
				{
					fout << " " << a[x];
				}
				fout << "\n";
				//cout << d<<"\n";
				cout << count;
				count++;
			}
			if (count == j)
				ch = false;
			else
			ch = true;
		}
	}
}