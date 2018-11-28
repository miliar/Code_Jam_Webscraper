#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

double c, f, x;
double eps = 1e-9;

double cnttm(int q)
{
	double v = 2;
	double st = 0;
	for(int i = 1; i <= q; ++i)
	{
		st += c / v;
		v += f;
	}
	st += x / v;
	return st;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("Boutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		cin >> c >> f >> x;
			 
		int ql = 0, qr = 100005, q;
		while(qr - ql > 1)
		{
			q = (qr + ql) / 2;
			if(cnttm(q + 1) > cnttm(q) + eps)
				qr = q;
			else
				ql = q;
		}
		
		printf("Case #%d: %.7lf\n", tt, min(cnttm(ql), cnttm(qr)));	
	}
	
	return 0;
}