#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <string>
#include <algorithm>
int l[20];
int compare(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int n, i, j, t, w, flag = 0, count = 0, k, s, s1 = 0, s2 = 0, rev, num, digit, s3, o, m;
	cin >> t;
	for (o = 0; o < t; o++)
	{
		flag = 0;
		for (i = 0; i <= 9; i++)
			l[i] = 0;
		cin >> n;
		for (i = 1; i <= 9999; i++)
		{
			s = n*i;
			num = s;
			do
			{
				digit = num % 10;
				l[digit]++;
				num = num / 10;
			} while (num != 0);
			count = 0;
			for (k = 0; k < 10; k++)
				if (l[k]>0)
					count++;
			if (count == 10)
			{
				cout << "Case #" << o + 1 << ": " << s << endl;
				flag = 1;
				break;
			}
		}
		if (flag == 0)
		{
			cout << "Case #" << o + 1 << ": " << "INSOMNIA" << endl;
			flag = 1;
		}
	}
	return 0;
}