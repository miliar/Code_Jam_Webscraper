#pragma comment(linker, "/STACK:64777216")
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<memory.h>
#include<ctime>
#include<cassert>

#define pb push_back
#define sz(a) (int)a.size()
#define bs binary_search
#define np next_permutation
#define mp make_pair
#define all(a) a.begin(),a.end()
#define read(a) scanf("%d", &a)
#define writeln(a) printf("%d\n", a);
#define forn(i, n) for (int i = 0; i < n; ++i)
#define forv(i, v) for (int i = 0; i < sz(v); ++i)
#define _(a, b) memset(a, b, sizeof a)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

template<class T> inline T sqr(T x) { return x * x; }

const double pi = acos(-1.0), eps = 1e-9;
const int INF = 1000 * 1000 * 1000;

int t, f, s, a[10][10], num = 0;

void prepare(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
#else
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

void solve()
{
	cin>> t;
	while (t) {
		vector<int> data;
		int cnt = 0, ans;
		--t;
		cin>> f;
		forn(i, 4)
			forn(j, 4)
				cin>> a[i][j];
		forn(i, 4)
			data.pb(a[f-1][i]);
		cin>> s;
		forn(i, 4)
			forn(j, 4)
				cin>> a[i][j];
		sort(all(data));
		forn(i, 4)
			if (bs(all(data), a[s-1][i])) {
				cnt++;
				ans = a[s-1][i];
			}
		cout<< "Case #"<< ++num<< ": ";
		if (cnt == 1) cout<< ans<< '\n';
		if (cnt == 0) cout<< "Volunteer cheated!\n";
		if (cnt > 1) cout<< "Bad magician!\n";
	}
}

int main()
{
	prepare("");

	solve();

	return 0;
}
