#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int M = 3000, N = 55;
string s[N];
set <string> ss;
vector <int> a[N];
map <string, int> ma;
int belong[M];
int org[M];

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";

		int n; cin >> n;
		cerr << n << endl;
		cin.get();
		for (int i = 0; i < n; i++) getline(cin, s[i]);

		ss.clear();
		ma.clear();
		for (int i = 0; i < n; i++) a[i].clear();

		for (int i = 0; i < n; i++)
		{
			string cur = "";
			for (char c : s[i])
			{
				if (c == ' ')
				{
					ss.insert(cur);
					cur = "";
				}
				else cur += c;
			}
			ss.insert(cur);
		}

		int sz = 0;
		for (string x : ss) ma[x] = sz++;

		for (int i = 0; i < n; i++)
		{
			string cur = "";
			for (char c : s[i])
			{
				if (c == ' ')
				{
					a[i].push_back(ma[cur]);
					cur = "";
				}
				else cur += c;
			}
			a[i].push_back(ma[cur]);

			sort(a[i].begin(), a[i].end());
			a[i].resize(unique(a[i].begin(), a[i].end()) - a[i].begin());
		}

		memset(org, -1, sizeof(org));
		for (int x : a[0]) org[x] = 0;
		for (int x : a[1])
			if (org[x] < 0) org[x] = 1;
			else org[x] = 2;

		int act = 0;
		for (int i = 0; i < M; i++)
			if (org[i] == 2)
				act++;

		int ret = 0x3f3f3f3f;
		for (int msk = 0; msk < 1 << (n - 2); msk++)
		{
			int nsk = msk;
			msk <<= 2;
			msk += 1;

			for (int i = 0; i < M; i++) belong[i] = org[i];
			int ct = act;
			for (int i = 2; i < n; i++)
				for (int x : a[i])
				{
					int cur;
					if (msk >> i & 1) cur = 0;
					else cur = 1;

					if (belong[x] < 0)
						belong[x] = cur;
					else if (belong[x] == 2)
						continue;
					else if (belong[x] != cur)
						belong[x] = 2, ct++;
				}
			ret = min(ret, ct);

			msk = nsk;
		}

		cout << "Case #" << tt << ": " << ret << "\n";
	}
	return 0;
}