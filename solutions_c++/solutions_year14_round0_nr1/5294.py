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

int v[105];

void work()
{
    int p, q;
    cin >> p;
    for (int i = 1; i < 17; ++i)
        v[i] = 0;
    for (int i = 1; i < 5; ++i)
        for (int j = 1; j < 5; ++j)
        {
            int x;
            cin >> x;
            if (i == p) ++v[x];
        }
    cin >> q;
    for (int i = 1; i < 5; ++i)
        for (int j = 1; j < 5; ++j)
        {
            int x;
            cin >> x;
            if (i == q) ++v[x];
        }
    int cnt = 0, ans = -1;
    for (int i = 1; i < 17; ++i)
        if (v[i] == 2) ++cnt, ans = i;
    if (cnt == 0) cout << "Volunteer cheated!" << endl;
    else if (cnt > 1) cout << "Bad magician!" << endl;
    else cout << ans << endl;
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	cin >> task;
	for (int i = 1; i <= task; ++i)
	{
	    cout << "Case #" << i << ": ";
	    work();
	}
	return 0;
}
