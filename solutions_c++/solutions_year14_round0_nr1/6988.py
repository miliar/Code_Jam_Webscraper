#pragma comment(linker, "/STACK:167177216")

#include<stdio.h>
#include<stack>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
#include<set>
#include<memory.h>
#include<vector>
#include<map>
#include<queue>
#include<iomanip>
#include<ctime>

using namespace std;

typedef long long li;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair

int r1, r2;
int a[4][4];

void read()
{
	cin >> r1;
	forn (i, 4)
		forn (j, 4)
		cin >> a[i][j];
	cin >> r2;
}

void solve()
{
	vector<int> v;
	forn (i, 4)
		v.push_back(a[r1 - 1][i]);
	forn (i, 4)
		forn (j, 4)
		cin >> a[i][j];
	int cnt = 0;
	int ans = -1;
	forn (i, 4)
		forn (j, 4)
		{
			if (v[i] == a[r2 - 1][j])
				cnt++, ans = v[i];
		}
	if (cnt == 1)
		cout << ans;
	if (cnt == 0)
		cout << "Volunteer cheated!";
	if (cnt != 0 && cnt != 1)
		cout << "Bad magician!";
}

int main()
{
#ifdef Baster
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	forn (i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		read();
		solve();
		cout << endl;
	}

	return 0;
}