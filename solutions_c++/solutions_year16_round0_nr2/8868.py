#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <string>
#include <algorithm>
int l[20];
char a[1000];
int compare(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int n, i, j,t,w,flag=0,count=0, k,s, s1=0,s2=0,rev,num,digit,s3,o, m;
	cin >> t;
	for (o = 0; o < t; o++)
	{
		count=0;
		cin >> a;
		n = strlen(a);
		for (i = n - 1; i >-1; i--)
		{
			if (a[i] == '+')
			{
				continue;
			}
			else if(a[i]=='-')
			{
				count++;
				for (j = i; j > -1; j--)
				{
					if (a[j] == '-')
						a[j] = '+';
					else
						a[j] = '-';
				}

			}
		}
		cout << "Case #" << o + 1 << ": " << count << endl;
    }
	return 0;
}