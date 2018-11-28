#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

bool equals(double a, double b)
{
	return abs(a-b) < 1e-12;
}

struct sc
{
	double v, x;
};

bool cmp(sc a, sc b)
{
	return a.x < b.x;
}

int main()
{
	int cn; cin >> cn;
	for (int cc=1; cc<=cn; cc++)
	{
		int n;
		double v, x;
		cin >> n >> v >> x;
		if (cc == 3)
			cerr << n << ' ' << v << ' ' << x << endl;

		vector<sc> vc(n);
		double engdif = 0.0, totalv = 0.0;
		int coldn = 0, hotn = 0;
		for (int i=0; i<n; i++)
		{
			cin >> vc[i].v >> vc[i].x;
			if (vc[i].x < x)
				coldn++;
			else if (vc[i].x > x)
				hotn++;
			if (cc == 3)
				cerr << vc[i].v << ' ' << vc[i].x << endl;
			vc[i].x -= x;
			engdif += vc[i].v * vc[i].x;
			totalv += vc[i].v;
		}

		if (coldn == n || hotn == n)
			goto IMP;

		sort(vc.begin(), vc.end(), cmp);

		for (int i=0; i<n && engdif < 0.0; i++)
			if (vc[i].v * vc[i].x > engdif)
			{
				totalv -= vc[i].v;
				engdif -= vc[i].v * vc[i].x;
			}
			else
			{
				totalv -= engdif / vc[i].x;
				engdif = 0.0;
			}

		for (int i=n-1; i>=0 && engdif > 0.0; i--)
			if (vc[i].v * vc[i].x < engdif)
			{
				totalv -= vc[i].v;
				engdif -= vc[i].v * vc[i].x;
			}
			else
			{
				totalv -= engdif / vc[i].x;
				engdif = 0.0;
			}

		if (equals(engdif, 0.0) && !equals(totalv, 0.0))
		{
			//cout.setf(ios::fixed);
			cout.precision(10);
			cout << "Case #" << cc << ": " << v / totalv << endl;
			if (cc == 3)
				cerr << v << ' ' << totalv << endl;
			continue;
		}
	IMP:
		cout << "Case #" << cc << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
