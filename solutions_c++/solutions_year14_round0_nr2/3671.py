#include<iostream>
#include<conio.h>
using namespace std;
void main()
{
	int T;
	long double C, F, X, m, n, p;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> C >> F >> X;
		p = 2;
		m = X / p;
		n = 0;
		while (m>=n)
		{
			p += F;
			n += C / (p - F);
			if (m > n+X/p)
				m = n+X/p;
			else
				break;
		}
		printf("Case #%d: %.7lf\n", i, m);
	}
}