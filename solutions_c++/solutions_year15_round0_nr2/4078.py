#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;
const int inf2 = 10000;
using namespace std;

int main (int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int j = 1; j <= T; ++j)
    {
        int D = 0;
        int ans = 0;
        scanf("%d", &D);
        vector<int> v(D), v1, v2;
        for (int i = 0; i < D; ++i)
        {
            scanf("%d", &v[i]);
            ans = max(ans, v[i]);
            v1.pb(v[i]);
            v2.pb(v[i]);
        }
        int habr = 0;
        for(;;)
        {
            if (v1.empty()) break;
            sort(v1.begin(), v1.end(), greater<int>());
            int cur = v1[0];
            int tt = habr + cur;
            ans = min(ans, tt);
			if (cur <= 3)
				break;
			if (cur == 6)
            {
				v1[0] = 3;
				v1.pb(3);
			}
			else if (cur == 9)
            {
				v1[0] = 3;
				v1.pb(6);
			}
			else if (!(cur % 2))
            {
				v1[0] = cur / 2;
				v1.pb(cur / 2);
			}
			else
            {
				v1[0] = cur / 2 + 1;
				v1.pb(cur / 2);
			}
			habr++;
		}
		habr = 0;
		for(;;)
        {
			if (v2.empty()) break;
			sort(v2.begin(), v2.end(), greater<int>());
			int cur = v2[0];
			int tt = habr + cur;
			ans = min(ans, tt);
			if (cur <= 3)
				break;
			if (!(cur % 2))
			{
				v2[0] = cur / 2;
				v2.pb(cur / 2);
			}
            else
            {
				v2[0] = cur / 2 + 1;
				v2.pb(cur / 2);
			}
			habr++;
		}
        printf("Case #%d: %d\n", j, ans);
        //for (int k = 0; k < D; ++k)
          //  cout << v[k] << " ";
        //cout << endl;
    }
    return 0;
}
