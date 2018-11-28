#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <string>
#include<math.h>
#include <algorithm>
int compare(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	unsigned long long int pos, n, c, i, j, t,kk, w, flag = 0, count = 0, k, s, s1 = 0, s2 = 0, rev, num, digit, s3, o, m;
	unsigned long long int a[10100];
	cin >> t;
	for (o = 0; o < t; o++)
	{
		pos = 0;
		cin >> k >> c >> s;
	for (i = 0, j = 1; i < s; j++, i++)
	{
		count = i;
			for (kk = 1; kk < c; kk++)
			{
				count = count*k;
				count += j-1;
			}
			a[i] = count + 1;
		}

		cout << "Case #" << o + 1 << ": ";
		for (i = 0; i < s; i++)
			cout << a[i] << " ";
		cout << endl;
	}
	return 0;
}