#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<queue>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t,n,m,i,c,a[10],j;
	cin >> t;
	j = 1;
	while (t--)
	{
		cin >> n;
		cout << "Case #" << j++ << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA\n";
			continue;
		}
		memset(a, 0, sizeof(a));
		c = 0;
		for (i = 1;; i++)
		{
			m = n*i;
			while (m > 0)
			{
				if (a[m % 10] == 0)
				{
					c++;
					a[m % 10] = 1;
				}
				m = m / 10;
			}
			if (c > 9) break;
		}
		cout << n*i << endl;
	}
}