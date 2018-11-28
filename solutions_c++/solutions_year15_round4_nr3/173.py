#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
const int nmax = 20 + 18, vmax = 10000 + 18, lmax = 10 + 18;

int V[vmax];
map<string, int> S;
bool eng[nmax];
vector<int> seqi[nmax];
int n, tot, ans;

int gethash(string s)
{
	if (S.find(s) == S.end())
		return S[s] = ++tot;
	else
		return S[s];
}

void search(int now)
{
	if (now > n) {
		int cnt = 0;
		for (int i = 1; i <= tot; ++i) V[i] = 0;
		for (int i = 1; i <= n; ++i) {
			int ns = eng[i] ? 2 : 1;
			for (int j = 0; j < seqi[i].size(); ++j)
				V[seqi[i][j]] |= ns;
		}
		for (int i = 1; i <= tot; ++i)
			if (V[i] == 3)
				++cnt;
		if (cnt < ans)
			ans = cnt;
		return;
	}
	eng[now] = 0;
	search(now + 1);
	eng[now] = 1;
	search(now + 1);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d\n", &n);
		memset(V, 0, sizeof(V));
		S.clear();
		tot = 0;
		for (int j = 1; j <= n; ++j) {
			seqi[j].clear();
			string tmp;
			getline(cin, tmp);
			for (int i = 0; i < tmp.size(); )
				if (tmp[i] != ' ') {
					string now = "";
					while (i < tmp.size() && tmp[i] != ' ')
						now.push_back(tmp[i++]);
					seqi[j].push_back(gethash(now));
//					cout << j << " " << now << " " << gethash(now) << endl;
				}
				else
					++i;
		}
		ans = tot;
		eng[1] = 1;
		eng[2] = 0;
		search(3);
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
