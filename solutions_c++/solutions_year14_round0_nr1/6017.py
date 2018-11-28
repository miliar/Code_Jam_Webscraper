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
	int c, f, p,n,T, v[4][4], vv[4][4];
	cin >> T;
	for (int i = 1; i <=T; ++i)
	{
		cin >> n;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> v[i][j];
		cin >> p;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> vv[i][j];
		cout << "Case #" << i << ": ";

		f = 0;
		c = 0;
		for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
				if (v[n-1][j] == vv[p-1][k])
				{
					++f;
					c = v[n-1][j];
				}
		if (f == 1)
			cout << c << endl;
		else if (f != 0)
			cout << "Bad magician!\n";
		else
			cout << "Volunteer cheated!\n";
	}
}
