#pragma comment(linker, "/STACK:256000000")

#include<stdio.h>
#include<stack>
#include<math.h>
#include<time.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<unordered_set>
#include<iomanip>
#include<memory.h>
#include<vector>
#include<map>
#include<cassert>
#include<queue>

using namespace std;

typedef long long li;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int a, b, k;

bool read()
{
	cin >> a >> b >> k;
	return true;
}

void solve()
{
	int ans = 0;
	forn (i, a)
		forn (j, b)
		if ((i & j) < k)
			ans++;
	cout << ans << endl;
}

int main()
{

#ifdef Baster
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
	forn (i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		read();
		solve();
	}
	return 0;
}