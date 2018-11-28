#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <ctime>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef pair<int, int> pii;
typedef long long int64;
typedef pair<int64, int64> pii64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;
typedef pair<int64,pii> piii64;
typedef pair<pii,pii> piiii;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa
#define y0 _sdkfsjfs__

#define tm _dskfjskdfjksdf

int n, nt, m;
int cnt[3];
int _cnt[3];
char alf[3] = {'P', 'R', 'S'};
int a[1 << 15];
vector<string> b;

inline int get_looser(int x)
{
	return (x + 1) % 3;
}

inline string get_tree(int st)
{
	if (!cnt[st]) return "Z";
	string res = "";
	for (int i = 0; i < 3; ++i)
		_cnt[i] = cnt[i];
	a[0] = st;
	--_cnt[st];
	for (int i = 0; i < m; ++i)
	{
		int c1 = (i << 1) + 1;
		int c2 = (i << 1) + 2;
		if (c1 >= m) continue;
		if (c2 >= m) continue;
		a[c1] = a[i];
		a[c2] = get_looser(a[i]);
		if (!_cnt[a[c2]]) return "Z";
		--_cnt[a[c2]];
	}
	for (int i = m - (1 << n); i < m; ++i)
		res += alf[a[i]];
	for (int t = 0; t < n; ++t)
	{
		b.clear();
		int len = (1 << t);
		for (int i = 0; i < (1 << n); i += len)
		{
			b.push_back(res.substr(i, len));
		}
		int k = (int)b.size();
		for (int i = 0; i < k; i += 2)
		{
			if (b[i] > b[i + 1])
				swap(b[i], b[i + 1]);
		}
		res = "";
		for (int i = 0; i < k; ++i)
			res += b[i];
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		int r, p, s;
		cin >> n >> r >> p >> s;
		m = (1 << (n + 1)) - 1;
		cnt[0] = p;
		cnt[1] = r;
		cnt[2] = s;
		string ans = "Z";
		for (int i = 0; i < 3; ++i)
			ans = min(ans, get_tree(i));
		if (ans == "Z")
			ans = "IMPOSSIBLE";
		cout << "Case #" << tn << ": " << ans << endl;
	}

    return 0;
}