#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
#define all(x) x.begin(), x.end()
typedef long long lng;
const int MOD = 10000007;
const double PI = 3.1415926;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        int Sm, ans = 0, stn = 0;
        string line;
        cin >> Sm >> line;
        for(int i = 0; i <= Sm; ++i)
        {
            if(stn >= i)
            {
                stn += (line[i] - 48);
            }
            else
            {
                ans += (i - stn);
                stn += (i - stn);
                stn += (line[i] - 48);
            }
        }
        cout << ans << endl;
    }
    return 0;
}
