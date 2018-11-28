#include<iostream>
#include<stdio.h>
#include <algorithm>
#include <string>
using namespace std;
double nao[1000], ken[1000];
int War(int n)
{
	int i,j,p;
	p = 0;
	j = 0;
	for (i = 0; i < n; i++)
	{
		for (; j < n;j++)
		{
			if (nao[j] > ken[i])
			{
				p++;
				j++;
				break;
			}
		}

	}
	return p;
}
int War_D(int n)
{
	int i,j, p;
	double a, b;
	p = 0;
	j = 0;
	sort(ken, ken + n);
	sort(nao, nao + n);
	for (i = 0; i < n; i++)
	{
		for (; j < n; j++)
		{
			if (nao[i] < ken[j])
			{
				p++;
				j++;
				break;
			}
		}

	}
	return p;
}
int main()
{
	//freopen("fun.out", "w", stdout);
	int p_d, p;
	int i,j,t,n;

    cin >> t;
	for (i = 1; i <=t; i++)
	{
 		cin >> n;
		for (j = 0; j < n; j++)
			cin >> nao[j];
		for (j = 0; j < n; j++)
			cin >> ken[j];

		p = n - War_D(n);
		p_d = War(n);
		cout << "Case #" << i << ": " << p_d << " " << p << endl;
	}

	return 0;
}
