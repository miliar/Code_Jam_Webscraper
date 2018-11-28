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

int a[100005], v[100005];

void work()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> a[i], v[i] = 0;
    sort(a, a + n);
    int ans = 0;
    for (int i = n - 1; i >= 0; --i)
    {
        if (v[i]) continue;
        v[i] = 1;
        ++ans;
        for (int j = i - 1; j >= 0; --j)
        {
            if (v[j]) continue;
            if (a[i] + a[j] <= m)
            {
                v[j] = 1;
                break;
            }
        }
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
