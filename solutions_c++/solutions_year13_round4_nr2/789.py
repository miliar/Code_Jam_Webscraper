#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

ll findmaxplace(int n, ll x) {
	if (x == 0)
		return 0;

	return (1L << (n-1)) + findmaxplace(n-1, (x-1) / 2);
}

ll findmax(int n, ll p) {
	ll l = 0;
	ll r = (1L << n) - 1;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		if (findmaxplace(n, m) > p) {
			r = m-1;
		} else
			l = m;
	}
	if (findmaxplace(n, r) > p)
		return l;
	else
		return r;
}

ll findminplace(int n, ll x) {
	if (x == (1L << n) - 1)
		return (1L << n) - 1;

	ll p = (1L << (n-1)) - 1;
	ll np = (1L << n)-1;
	ll nr = (np - x - 1) / 2;
	return findminplace(n-1, p - nr);

}

ll findmin(int n, ll p) {
	ll l = 0;
	ll r = (1L << n) - 1;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		if (findminplace(n, m) > p) {
			r = m-1;
		} else
			l = m;
	}
	if (findminplace(n, r) > p)
		return l;
	else
		return r;
}

void testcase(int tst)
{
	int n;
	ll p;
	ifs >> n >> p;
	p--;

	ofs << "Case #" << tst+1 << ": " << findmax(n, p) << ' ' << findmin(n, p) << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
