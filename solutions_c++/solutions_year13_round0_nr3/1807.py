/**											Be name Khoda											**/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <bitset>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <memory.h>
using namespace std;

#define ll long long
#define un unsigned
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define VAL(x) #x << " = " << x << "   "
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) x.size())
#define ALL(x) x.begin(), x.end()
#define CLR(x, a) memset(x, a, sizeof x)
#define FOREACH(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define X first
#define Y second
#define SAL cerr << "Salam!\n"
#define PI (3.141592654)

//#define cout fout
//#define cin fin

//ifstream fin("problem.in");
//ofstream fout("problem.out");

const int MAXN = 1000 * 1 + 10, INF = 1e9 + 10;

bool isPalind(ll n)
{
	vector<int> v;
	while (n != 0)
	{
		v.pb(n % 10);
		n /= 10;
	}
	for (int i = 0, j = SZ(v) - 1; i < SZ(v); i ++, j --)
		if (v[i] != v[j])
			return false;
	return true;
}

bool isSqr(ll n)
{
	ll tmp = sqrt(n);
	if (SQR(tmp) == n)
		return true;
	else return false;
}

bool check(ll n)
{
	if (!isSqr(n))
		return false;
	ll tmp = sqrt(n);
	if (isPalind(tmp))
		return true;
	return false;
}

vector<ll> fair;
vector<int> v;

void build(int len)
{
	if (SZ(v) == (len + 1) / 2)
	{
		vector<int> tmp = v;
		ll res = 0;
		for (int i = 0; i < SZ(v); i ++)
			res = res * 10 + v[i];
		if (len % 2 == 1)
			v.pop_back();
		reverse(ALL(v));
		for (int i = 0; i < SZ(v); i ++)
			res = res * 10 + v[i];
		if (check(res))
			fair.pb(res);
		v = tmp;
		return ;
	}
	for (int i = 0; i < 10; i ++)
	{
		if (SZ(v) == 0 && i == 0)
			continue;
		v.pb(i);
		build(len);
		v.pop_back();
	}
}

int main ()
{
	ios::sync_with_stdio(false);
	for (int i = 1; i <= 14; i ++)
		build(i);
	//FOREACH(i, fair) cout << *i << endl;
	//cout << SZ(fair) << endl;
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t ++)
	{
		ll a, b;
		int ans = 0;
		cin >> a >> b;
		for (int i = 0; i < SZ(fair); i ++)
			if (fair[i] >= a && fair[i] <= b)
				ans ++;
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

