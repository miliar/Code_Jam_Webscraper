#include<iostream>
#include<stdlib.h>
#include<stdio.h>

using namespace std;
int gen(int p, int q)
{
	if (q == 0)
		return -1;

	int qpower = 0;
	while ((q % 2 == 0))
	{
		q = q / 2;
		qpower++;
	}
	
	if (p % q != 0)
	{
		return -1;
	}

	p = p / q;
	
	int ppower = 0;
	int ppowered = 1;

	while (true)
	{
		if (ppowered * 2 < p)
		{
			ppower++;
			ppowered *= 2;
		}
		else
		{
			break;
		}
	}

	if (ppower > qpower)
	{
		return -1;
	}

	return qpower - ppower;
}

int main()
{
	int t = 0;
	cin >> t;
	for (int a = 1; a <= t; a++)
	{
		int p, q;
		cin >> p;
		cin >> q;
		int gene = gen(p, q);
		cout << "Case " << "#" << a << ":" << " ";
		if (gene == -1)
		{
			cout << "impossible" << endl;
		}
		else
		{
			cout << gene << endl;
		}
	}
	return 0;
}