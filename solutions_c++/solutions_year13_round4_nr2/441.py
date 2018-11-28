#pragma comment(linker, "/STACK:256000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back                      
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define pi 3.1415926535897932

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

ll calc(int n, ll p)
{
	int c = 1;

	ll pw = (1LL << (n - 1));

	while (p > pw)
	{
		c++;
		p -= pw;
		pw /= 2;
	}	

	return (1LL << c) - 2;
}

void solve(int test)
{
	printf("Case #%d: ", test);

	int n; ll p;
	cin >> n >> p;

	if (p == (1LL << n))
	{
		cout << (1LL << n) - 1 << " " << (1LL << n) - 1 << endl;
		return;
	}

	cout << calc(n, p) << " " << (1LL << n) - calc(n, (1LL << n) - p) - 2 << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc; scanf("%d\n", &tc);

    forn(it, tc) solve(it + 1);

    return 0;
}
