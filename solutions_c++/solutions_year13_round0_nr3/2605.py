#include <iostream>
#include <cmath>
#include <deque>
#include <algorithm>
#include <map>
#include <cstdio>
#include <sstream>
#include <deque>

using namespace std;

#define MAXN 12000
#define pi pair <int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())

using namespace std;

typedef deque<int> VI;
typedef deque<VI> VVI;
typedef long long ll;
typedef deque<ll> VL;
typedef deque<VL> VVL;
typedef double D;
typedef deque<D> VD;
typedef deque<VD> VVD;
typedef pair<int, int> PI;
typedef deque<PI> VPI;

int T;
ll A, B, p10[20];
VL v[20], d;
int cnt, MAXS = 7;

int check ( ll n )
{
	n *= n;
	VI a;

	while (n)
	{
		a.pb(n%10LL);
		n /= 10LL;
	}

	while (sz(a) >= 2)
	{
		if(a.front() != a.back())
			return 0;
		a.pop_back();
		a.pop_front();
	}
	return 1;
}

int find ( ll n, int lo = 0, int hi = sz(d)-1 )
{
	if (hi == lo)
	{
		if ( n < d[lo] )
			return lo-1;
		else
			return lo;
	}
	int mid = hi-(hi-lo)/2;
	if ( n < d[mid] )
		return find(n, lo, mid-1);
	return find(n, mid, hi);
}

int main (int argc, char const* argv[])
{
	p10[0] = 1;
	for (int i = 1; i < 17; i += 1)
	{
		p10[i] = p10[i-1]*10LL;
	}

	v[0].pb(0);
	for (int i = 1; i < 10; i += 1)
		v[1].pb(i);
	for (int l = 2; l <= MAXS; l += 1)
	{
		for (int a = 1; a <= 9; a += 1)
		{
			for (int i = 0; i < sz(v[l-2]); i += 1)
			{
				v[l].pb(((ll)a)*(p10[l-1]+1LL)+10LL*v[l-2][i]);
			}
		}
	}

	for (int i = 1; i <= MAXS; i += 1)
	{
		for (int j = 0; j < sz(v[i]); j += 1)
		{
			if(check(v[i][j]))
				d.pb(v[i][j]);
		}
	}

	cin >> T;

	for (int cs = 1; cs <= T; cs += 1)
	{
		cin >> A >> B;
		A = (int)(sqrt(A-1));
		B = (int)(sqrt(B));
		cout << "Case #" << cs << ": " << find(B)-find(A) << '\n';
	}
	
	
	return 0;
}










