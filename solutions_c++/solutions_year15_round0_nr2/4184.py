#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
inline int small(int a[1000],int d,int hav)
{
	int max = a[0], min = 0, count = 0, ex, re, max1, hav1,sq;
	int l[1000],li[1000],ans,count1=0;
		for (int j = 1; j < d; j++)
		{
			if (max < a[j])
			{
				max = a[j];
			}
		}
		max1 = 0;
		for (int j = 0; j < d; j++)
		{
			if (max == a[j])
			{
				count++;
			}
		}
		for (int j = 0; j < d; j++)
		{
			if (max != a[j])
			{
				if (max1 < a[j])
					max1 = a[j];
			}
		}
		for (int j = 0; j < d; j++)
		{
			if (max1 == a[j])
			{
				count1++;
			}
		}
		if (!(count >= max / 2))
		{
				for (int j = 0; j < d; j++)
				{
					if (max == a[j])
					{
						if (max == 9 &&((max1==6&&count1<3)||max1<=3)&&count<=2)
						{
							a[d] = 3;
							a[j] = 6;
						}
						else
						{
							re = a[j] % 2;
							a[d] = a[j] / 2;
							a[j] = a[j] / 2 + re;
						}
						d++;
					}
				}
				hav = hav + count;
				for (int j = 0; j < d; j++)
				{
					l[j] = a[j];
				}
				ex = small(a, d, hav);

				max = l[0];
				for (int j = 1; j < d; j++)
				{
					if (max < l[j])
					{
						max = l[j];

					}
				}
				min = hav + max;

				if (ex < min)
				{
					return ex;
				}
				else
				{
					return min;
				}
		}

		return max + hav;
}
void main()
{
	int t, n, p, s[1000] ,d;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{

		fin >> d;
		for (int j = 0; j < d; j++)
		{
			fin >> s[j];
		}
		p = small(s,d,0);
		
		fout << "Case #" << i << ": " << p << "\n";
	}
}