#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

char save[5000];

int main()
{
 /*   freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
   */ std::ios::sync_with_stdio(false);
    int t;
    cin >> t;
    int cas = 0;
    int up;
    while (cas ++ < t)
    {
        cin >> up;
        cin >> save;
        int i;
        int res = 0;
        int cnt = 0;
        for (i = 0; i <= up; i++)
        {
            if (cnt >= i)
            {
                cnt += save[i] - '0';
            }
            else
            {
                res += i-cnt;
                cnt = i + save[i] - '0';
            }
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
