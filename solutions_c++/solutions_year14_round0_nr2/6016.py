#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#define EPS 0.0000000000000001
#define fori(N) for(i = 0; i < N; ++i)
#define forid(N) for(int i = 0; i < N; ++i)
#define forj(N) for(j = 0; j < N; ++j)
#define forjd(N) for(int j = 0; j < N; ++j)

using namespace std;

int gcd(int a, int b) {return (b = 0 ? a : gcd(b, a%b));}
int lcm(int a, int b) {return (a * (b / gcd(a, b))); }

struct pto
{
	double x;
	double y;
	pto(){}
	pto(double _x, double _y){ x = _x; y = _y;}
};

int main()
{
	int T;
	double c, f, x;
	cin >> T;
	double Time;
	for (int i = 1; i <= T; ++i)
	{
		Time = 0;
		double cps = 2;
		cout << "Case #" << i << ": ";
		cin >> c >> f >> x;
		int nc = 0;
ini:	double t1 = x/cps;
		double t3 = c/cps + x/(cps + f);
		if (t3 < t1)
		{
			++nc;
			Time = Time + c/cps;
			cps = cps+f;
			goto ini;
		}
		else
			Time+=t1;
		printf("%.7f\n", Time);
	}
}
