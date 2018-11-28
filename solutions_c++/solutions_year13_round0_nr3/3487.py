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

vector<ll> nums;

void testcase(int tst)
{
	ll a, b;
	ifs >> a >> b;
	int res = 0;
	REP(i, nums.sz)
		if (nums[i] >= a && nums[i] <= b) res++;

	ofs << "Case #" << tst+1 << ": " << res << endl;
}

VI getarray(ll i) {
	VI a; 
	while (i > 0) {
		a.pb(i%10);
		i /= 10;
	}
	return a;
}

void trypalindrome(VI b) {
	ll k = 1;
	ll n = 0;
	REP(i, b.sz) {
		n += k * b[i];
		k *= 10;
	}

	n = n*n;
	VI a = getarray(n);

	bool ok = true;
	REP(i, a.sz / 2)
		if (a[i] != a[a.sz-1-i])
			ok = false;
	if (ok)
		nums.pb(n);
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	REP(n, 10000) {
		if (n == 0) continue;

		VI a = getarray(n); 

		VI b = a;
		for (int i = b.sz - 1; i >= 0; i--)
			b.pb(b[i]);

		trypalindrome(b);

		b = a;
		for (int i = b.sz - 2; i >= 0; i--)
			b.pb(b[i]);

		trypalindrome(b);
	}

	sort(ALL(nums));

	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
