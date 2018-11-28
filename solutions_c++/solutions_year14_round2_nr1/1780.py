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

int n;
vector<string> v;

bool read()
{
	cin >> n;
	v.resize(n);
	forn (i, n)
		cin >> v[i];
	return true;
}

void solve()
{
	set<string> s;
	vector<pair<char, int> > a[100];
	forn (i, n)
	{
		string cur = "";
		int l = 0;
		while (l < v[i].size())
		{
			int r = l;
			while (r < v[i].size() && v[i][r] == v[i][l])
				r++;
			a[i].push_back(mp(v[i][l], r - l));
			cur += v[i][l];
			l = r;
		}
		s.insert(cur);
	}
	if (s.size() != 1)
	{
		cout << "Fegla Won" << endl;
		return;
	}
	int ans = 0;
	forn (i, a[0].size())
	{
		int sum = 0;
		forn (j, n)
			sum += a[j][i].second;
		int tot = 1.0 * sum / n + 0.5;
		forn (j, n)
			ans += abs(tot - a[j][i].second);
	}
	cout << ans << endl;
}

int main()
{

#ifdef Baster
	freopen("A-small-attempt0.in", "rt", stdin);
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