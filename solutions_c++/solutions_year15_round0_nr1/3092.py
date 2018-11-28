#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const double eps = 1e-8;

int main()
{
   // #ifndef ONLINE_JUDGE
    	freopen("A-large.in","r",stdin);
    	freopen("A-large.out","w",stdout);
    //#endif
    string S;
    int T, cas = 1;
    cin >> T;
    while (T--)
    {
        int n;
        scanf ("%d", &n);
        cin >> S;
        int len = S.size();
        ll ans = 0, cnt = 0;
        for (int i = 0; i < len; i++)
        {
            if (S[i]>'0')
            {
                ans += max((ll)0, (ll)i-cnt);
                cnt += max((ll)0, (ll)i-cnt) + S[i]-'0';

            }
        }
        printf("Case #%d: ", cas++);
        cout << ans << endl;
    }
    return 0;
}
