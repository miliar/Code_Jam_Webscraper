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
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	scanf("%d", &tests);

	int used[17];
	rep(test, tests)
	{
		C(used);
		int a, r;
		vint res;
		res.clear();

		scanf("%d", &r);
		rep(j, 4)
			rep(i, 4)
			{
				scanf("%d", &a);
				if (j + 1 == r)
					used[a]++;
			}

		scanf("%d", &r);
		rep(j, 4)
			rep(i, 4)
			{
				scanf("%d", &a);
				if (j + 1 == r)
					used[a]++;
				if (used[a] == 2)
					res.pb(a);
			}

		printf("Case #%d: ", test + 1);
		if (sz(res) == 1)
			printf("%d\n", res[0]);
		else if (sz(res) > 1)
			printf("Bad magician!\n");
		else //if (sz(res) < 1)
			printf("Volunteer cheated!\n");
	}	

	return 0;
}
