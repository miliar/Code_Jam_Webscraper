#pragma comment(linker, "/STACK:255000000")
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <stack>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <valarray>
#include <complex>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef complex<double> comp;

long double eps = 1e-7;
const int BASE = (int) 1e9;
const long double PI = 3.1415926535897932384626433832795;
const int MOD = (int) 1e9 + 7;
const int HMOD = (1 << 18) - 1;
const int N = 4000000;
const int INF = 1 << 30;
const LL LLINF = 1ll << 60;

int t;
double c, f, x;

double F(double f1, int it)
{
	if (it > 500000)
		return x / f1;
	double res = min(F(f1 + f, it + 1) + c / f1, x / f1); 
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		printf("Case #%d: %.7lf\n", k + 1, F(2.0, 0));
	}
	return 0;
}