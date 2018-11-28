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

int n, x;
int a[10000];


bool read()
{
	cin >> n >> x;
	forn (i, n)
		cin >> a[i];
	return true;
}

void solve()
{
	sort(a, a + n);
	reverse(a, a + n);
	int l = 0, r = n - 1;
	int ans = 0;
	while (l <= r)
	{
		int cur = x;
		int cnt = 0;
		ans++;
		while (a[l] <= cur && cnt < 2)
			cur -= a[l++], cnt++;
		while (a[r] <= cur && cnt < 2)
			cur -= a[r--], cnt++;
	}
	cout << ans << endl;
}

int main()
{

#ifdef Baster
	freopen("A-large.in", "rt", stdin);
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