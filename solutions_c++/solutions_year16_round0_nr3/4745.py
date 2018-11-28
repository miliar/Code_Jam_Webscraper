#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
#include <fstream>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define INF 1000000000
const double PI = acos(-1.0);

typedef long long ll;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;


ll convertFrom(int base, ll n)
{
	ll res = 0;
	ll b = 1;
	while(n)
	{
		if (n&1) res += b;
		b*=base;
		n >>= 1;
	}
	return res;
}

string show(int n)
{
	string res = "";
	while(n)
	{
		if (n&1) res.push_back('1');
		else res.push_back('0');
		n >>= 1;
	}
	reverse(ALL(res));
	return res;
}

vector<pair<ll, vector<ll> > > result;

vector<ll> partial;

bool check(ll n, int base)
{
	//cerr << "Check in base" << base << endl;
	for (ll i = 2; i*i <= n; ++i)
	{
		if ((n%i)==0) {
			partial[base] = i;
			return false;
		}
	}
	return true;
}

void solve()
{
	int a,b;
	cin >> a >> b;
	int N = 1 << (a-2);
	for (int mask = 6000; mask < N; ++mask)
	{
		int n = (mask + N)*2+1;
		cerr << mask << "/" << N << endl;

		partial.resize(11);
		bool ok = true;
		for (int i = 2; i <= 10; ++i)
		{
			if (check(convertFrom(i,n), i))
				ok = false;
		}
		if (ok)
			result.push_back(MP(n,partial));
		if (result.size() >= b)
			break;
	}

	for (int i = 0; i < result.size(); ++i)
	{
		cout << endl;
		cout << show(result[i].first);
		for (int j = 2; j <= 10; ++j)
		{
			cout << " " << result[i].second[j];
		}
	}
	cout << endl;
	/*
	cout << endl << endl << endl;
	for (int i = 0; i < result.size(); ++i)
	{
		cout << endl;
		cout << show(result[i].first) << endl;
		for (int j = 2; j <= 10; ++j)
		{
			cout << convertFrom(j, result[i].first) << " " << result[i].second[j] << endl;
		}
		cout << endl;
	}
	cout << endl;
	*/
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; ++test)
	{
		cerr << "Test: " << test << endl;
		printf("Case #%d: ", test);
		solve();
	}
	return 0;
}