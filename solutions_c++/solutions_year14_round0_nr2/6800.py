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

int t, num = 1;
double c, f, x, farm[100005], grow[100005], tm[100005];

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
		--t;
		_(tm, 0);
		double cost = 2;
		cin>> c>> f>> x;
		farm[0] = 0;
		grow[0] = x / cost;
		farm[1] = c / cost;
		cost += f;
		grow[1] = x / cost;
		for (int i=2; i<=100000; i++) {
			farm[i] = farm[i-1] + c / cost;
			cost += f;
			grow[i] = x / cost;
		}
		for (int i=0; i<=100000; i++)
			tm[i] = farm[i] + grow[i];
		sort(tm, tm + 100000);
		cout<< "Case #"<< num++<< ": ";
		printf("%.7lf\n", tm[0]);
	}
}

int main()
{
	prepare("");

	solve();

	return 0;
}
