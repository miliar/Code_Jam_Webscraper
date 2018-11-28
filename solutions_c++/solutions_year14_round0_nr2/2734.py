#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define all(x) (x).begin(), (x).end()
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define op operator
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef long long i64;

const double eps = 1.0e-9;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double cur_time = 0.0;
		double cur_speed = 2.0;
		double best;
		int X1 = X;
		fore(farms, 0, X1)
		{
			double nnew = cur_time + X / cur_speed;
			if (farms == 0 || best - nnew > eps)
			{
				best = nnew;
			}
			cur_time += C / cur_speed;
			cur_speed += F;
		}
		printf("Case #%d: %.10lf\n", test, best);
	}

	return 0;
}