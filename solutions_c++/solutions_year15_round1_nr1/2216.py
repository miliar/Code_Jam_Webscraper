#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int a[1000];
int b[1000];
long long int find1(int m)
{
	int i,min=b[0];
	long long int x = 0;
	for (i = 0; i < m - 1; i++)
	{
		if (b[i] < min)
			min = b[i];
	}
	for (i = 0; i < m-1; i++)
	{
		if (a[i] >= abs(min))
		x += abs(min);
		else
		x += a[i];
	}
	return x;
}
long long int find2(int m)
{
	int i;
	long long int y = 0;
	for (i = 0; i < m - 1; i++)
		if (b[i] < 0)
			y = y + abs(b[i]);
	return y;
}
int main()
{
	int t, f = 1, m, i; // change these
	long long int x, y;
	cin >> t;
	while (t > 0)
	{
		int j = 0;
		cin >> m;
		
		for (i = 0; i < m; i++)
		{
			cin >> a[i];
		}
		for (j = 0; j < m-1; j++)
		{
			b[j] = a[j + 1] - a[j];
		}
		x = find1(m);
		y = find2(m);
		printf("Case #%d: %lld %lld\n", f++, y,x);
		t--;
	}
	_getch();
}