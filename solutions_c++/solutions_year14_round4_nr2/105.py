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

#define x first
#define y second

struct node
{
    int x, y;
    bool operator<(const node &b) const
    {
        return x < b.x;
    }
};

node a[1005];

void work()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i].x;
        a[i].y = i;
    }
    sort(a, a + n);
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int l = 0, r = 0;
        for (int j = i + 1; j < n; ++j)
        {
            if (a[j].y > a[i].y) ++l;
            if (a[j].y < a[i].y) ++r;
        }
        ans += min(l, r);
    }
    cout << ans << endl;
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
