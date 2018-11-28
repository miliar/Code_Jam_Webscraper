#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(v) v.begin(), v.end()

map< vector<int>, int > d;

int get(vector<int> x)
{
	sort(all(x));
	if (d.count(x))
		return d[x];
	int n = x.size();
	if (!n)
		return 0;
	vector<int> xminus;
	forn(i, n)
		if (x[i] > 1)
			xminus.push_back(x[i] - 1);
	int res = 1 + get(xminus);
	vector<int> y(n + 1, 0);
	forn(i, n)
		y[i] = x[i];
	forn(i, n) {
		if (x[i] <= 3)
			continue;
		forn(j, x[i]) {
			if (j > x[i] - j)
				break;
			if (j > 1) {
				y[i] = j;
				y[n] = x[i] - j;
				res = min(res, 1 + get(y));
				y[i] = x[i];
			}
		}
	}
	return d[x] = res;
}

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tt, n;
	vector<int> a;
	cin >> tt;
	a.reserve(24);
	forn(tc, tt) {
		cin >> n;
		a.resize(n);
		forn(i, n) {
			scanf("%d", &a[i]);
		}
		int res = get(a);
		cerr << tc << endl;
		printf("Case #%d: %d\n", tc+1, res);
	}

	/*int tt, n;
	cin >> tt;
	string s;
	forn(tc, tt) {
		cin >> n >> s;
		++n;
		int res = 0, c = 0;
		forn(i, n) {
			if (s[i] > '0' && c < i) {
				res += i - c;
				c = i;
			}
			c += s[i] - '0';
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
	*/
}