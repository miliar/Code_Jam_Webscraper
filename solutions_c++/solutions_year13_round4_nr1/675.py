#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(i, a, n) for(int i=(a), __ ## i=(n); i<__ ## i; i++)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";if(sz(X))cout<<*(X).end();cout<<"}"<<endl;}

template<class T> ostream &operator<<(ostream &os, vector<T> &vec) {
	os << '{';
	REP(i, sz(vec))
	{
		os << vec[i];
		if (i + 1 != sz(vec) )
			os << ',';
	}
	os << '}';
	return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os,
		pair<T1, T2> &par) {
	os << '(' << par.X << ',' << par.Y << ')';
	return os;
}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

int gcd(int x, int y) {
	return y ? gcd(y, x % y) : abs(x);
}

template<class T> T sqr(T x) {
	return x * x;
}

const int NUM = 2200;
pair<PII, int> a[NUM];
int st[NUM];

const int MOD = 1000002013;

lint dist(lint from, lint to, lint num) {
	lint d = to - from;
	return (d * (d - 1) / 2) % MOD * num;
}

void solve(int test) {
	int n, m;
	cin >> n >> m;
	lint ans = 0;
	REP(i, m)
	{
		lint from, to, num;
		cin >> from >> to >> num;
		ans = (ans - dist(from, to, num)) % MOD;
		a[i * 2] = mp(mp(from, -1), num);
		a[i * 2 + 1] = mp(mp(to, 1), num);
	}

	sort(a, a + m * 2);

	int stn = 0;
	for (int i = 0; i < m * 2; ++i) {
		if (a[i].X.Y == -1) {
			st[stn++] = i;
		} else {
			while (a[i].Y) {
				int top = st[stn - 1];
				int from = a[top].X.X;
				int to = a[i].X.X;
				int num = min(a[top].Y, a[i].Y);
				ans = (ans + dist(from, to, num)) % MOD;
				a[top].Y -= num;
				a[i].Y -= num;
				if (a[top].Y == 0)
					--stn;
			}
		}
	}

	ans = (ans + MOD) % MOD;

	cout << "Case #" << test << ": ";
	cout << fixed;
	cout << setprecision(8);
	cout << ans;
	cout << endl;
}

void pre() {
}

int main() {
    if (!freopen("1.in", "r", stdin))
    {
        cerr << "No input file" << endl;
        return 1;
    }
    if (!freopen("1.out", "w", stdout))
    {
        cerr << "Error creating output file" << endl;
        return 1;
    }
	ios::sync_with_stdio(false);
	pre();
	int n;
	cin >> n;
	string tmp;
	getline(cin, tmp);
	for (int i = 1; i <= n; ++i) {
		solve(i);
	}
	return 0;
}
