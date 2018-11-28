#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <ctime>
#include <sstream>
#include <fstream>
#include <bitset>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long int64;

#define mp make_pair
#define PII pair<int, int>
#define pb push_back
#define sz(X) ((int)((X).size()))

#define x0 first0
#define y0 second0
#define x1 first1
#define y1 second1

const int N = 1005;

int ans0, ans1, n, m, b[N];
vector<string> a[N];
string s[N];

int cal(string s, string t)
{
    int ret = 0;
    for (int i = 0; i < sz(s) && i < sz(t); ++i)
    {
        if (s[i] != t[i]) return ret;
        ++ret;
    }
    return ret;
}

void dfs(int i)
{
    if (i == n)
    {
        for (int j = 0; j < m; ++j)
            a[j].clear();
        for (int j = 0; j < n; ++j)
            a[b[j]].pb(s[j]);
        int tmp = 0;
        for (int j = 0; j < m; ++j)
        {
            if (sz(a[j]) == 0) return;
            sort(a[j].begin(), a[j].end());
            for (int k = 0; k < sz(a[j]); ++k)
            {
                tmp += a[j][k].size();
                if (k)
                    tmp -= cal(a[j][k - 1], a[j][k]);
            }
            tmp++;
        }
        if (tmp > ans0)
        {
            ans0 = tmp;
            ans1 = 1;
        }
        else if (tmp == ans0)
        {
            ++ans1;
        }
        return;
    }
    for (int j = 0; j < m; ++j)
    {
        b[i] = j;
        dfs(i + 1);
    }
}

void work()
{
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> s[i];
    ans0 = -1;
    ans1 = 0;
    dfs(0);
    cout << ans0 << ' ' << ans1 << endl;
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	cin >> task;
	for (int tt = 1; tt <= task; ++tt)
	{
	    cout << "Case #" << tt << ": ";
	    work();
	}
	return 0;
}
