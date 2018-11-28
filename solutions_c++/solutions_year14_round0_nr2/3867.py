#define _CRT_SECURE_NO_DEPRECATE

#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <ctime>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int main()
{
	freopen("B-large.in", "r", stdin);
	// freopen("input.txt", "r", stdin);
	freopen("outputBlar.txt", "w", stdout);

	int tests, N;
	double C, F, X, res1, res2;
	scanf("%d\n", &tests);
	rep(test, tests)
	{
		scanf("%lf %lf %lf", &C, &F, &X);

		N = int(X / C - 1 - 2.0 / F);
		if (N < 0)
			N = 0;
		
		res1 = 0.0;
		rep(i, N)
			res1 += C / (2.0 + F * i);
		res1 += X / (2.0 + F * N);

		N++;
		res2 = 0.0;
		rep(i, N)
			res2 += C / (2.0 + F * i);
		res2 += X / (2.0 + F * N);

		printf("Case #%d: %.7lf\n", test + 1, min(res1, res2));
	}

	return 0;
}
