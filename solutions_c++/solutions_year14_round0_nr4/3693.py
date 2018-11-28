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

int tests, n, fair, cheat, j;
vector<double> a1, a2, ca1, ca2;
double a;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output_big.txt", "w", stdout);

	scanf("%d", &tests);
	rep(test, tests)
	{
		a1.clear();
		a2.clear();
		fair = cheat = 0;

		scanf("%d", &n);
		rep(i, n)
		{
			scanf("%lf", &a);
			a1.pb(a);
		}
		rep(i, n)
		{
			scanf("%lf", &a);
			a2.pb(a);
		}

		sort(all(a1));
		sort(all(a2));

		ca1 = a1;
		ca2 = a2;

		ROF(i, n - 1, 0)
		{
			if (a1[i] > a2[i])
			{
				fair++;
				a1.pop_back();
				a2.erase(a2.begin());
			}
			else
			{
				a1.pop_back();
				a2.pop_back();
			}
		}

		a1 = ca1;
		a2 = ca2;

		int j = 0;
		rep(i, n)
		{
			while (j < n && a1[j] < a2[i])
				j++;
			if (j < n)
			{
				cheat++;
				j++;
			}
			else
				break;
		}

		printf("Case #%d: %d %d\n", test + 1, cheat, fair);
	}

	return 0;
}
