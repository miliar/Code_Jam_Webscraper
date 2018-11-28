#include<stdio.h>
#include <iostream>
#include<vector>
char a[200000],b[200000];
using namespace std;
int  main()
{          freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
	int x[1000], x1[1000], o, t, y1[1000], y[1000], n, i, j, m, k, l, sum = 0;
	cin >> t;
	for (o = 0; o < t; o++)
	{		cin >> a;
	k = 1500, n = 1500, m = 1500;
	b[k] = a[0];
	for (i = 1; a[i] != '\0'; i++)
	{
		if (a[i] < b[m])
			b[++n] = a[i];
		else
			b[--m] = a[i];
	}
	cout << "Case #" << o + 1 << ": ";
	for (i = m; i <= n; i++)
		cout << b[i];
	cout << endl;
    }
	return 0;
}