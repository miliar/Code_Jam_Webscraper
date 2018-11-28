#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>
using namespace std;

int cmp(const void*x, const void*y)
{
	double a = *(double*)x;
	double b = *(double*)y;

	if (a > b)
		return 1;
	else if (a < b)
		return -1;
	return 0;

}


int main()
{
	int test, index,first,second,x,y,w,d,n;
	double a[1002],b[1002];

	fstream fp("B-small-practice.in", ios::in);
	fstream op("B-small-practice.out", ios::out);

	
	index = 0;
	fp >> test;
	while (test--)
	{

		fp >> n;
		for (int i = 0; i < n; i++)
			fp >> a[i];
		for (int i = 0; i < n; i++)
			fp >> b[i];

		qsort(a, n, sizeof(double), cmp);
		qsort(b, n, sizeof(double), cmp);


		x = y = n - 1;
		first = second = w=d=0;

		while ((first <= x) && (second <= y))
		{
			if (a[x] < b[y])
			{
				x--;
				y--;
			}
			else
			{
				w++;

				if (second < y)
				{
					second++;
					x--;
				}
				else
				{
					x--;
					y--;

				}

			}

		}

		x = y = n - 1;
		first = second = d = 0;

		while ((first <= x) && (second <= y))
		{
			if (a[x] > b[y])
			{
				d++;
				x--;
				y--;
			}
			else
			{

				if (first < x)
				{
					first++;
					y--;
				}
				else
				{
					x--;
					y--;

				}

			}



		}

		index++;
		op << "Case #" << index << ": " << d << " "<<w<< endl;
		


	}

}