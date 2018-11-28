#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <list>
#include <ctime>

#define x first
#define y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ld, ld> point;
typedef pair<int, int> pii;
typedef pair<pii, int> ppi;
typedef pair<ll, ll> pll;
typedef pair<string, string> pss;
typedef vector<int> lint;

const int N = (int)(3e5) + 7;
const ll MD = 1000000000;
const int KOL = 9;
const int M = (int)(1e6) + 7;
const ll INF = (ll)(1e9) + 7;
const ll MOD = (ll)(1e9) + 7;
const ld eps = 1e-12;

int a[20];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int n;
	cin >> n;
	for (int ii = 0; ii < n; ++ii)
	{
		vector<int> v;
		v.clear();
		for (int i = 0; i < 20; ++i)
			a[i] = 0;
		int x;
		cin >> x;
		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				int q;
				cin >> q;
				if (i == x)
					a[q]++;
			}
		}
		cin >> x;
		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				int q;
				cin >> q;
				if (i == x)
					a[q]++;
			}
		}
		for (int i = 0; i < 20; ++i)
			if (a[i] == 2)
				v.pb(i);
		printf("Case #%d: ", ii + 1);
		if (!(int)(v.size()))
			cout << "Volunteer cheated!\n";
		else
			if ((int)(v.size()) > 1)
				cout << "Bad magician!\n";
			else
				cout << v[0] << endl;
	}
	return 0;
}
