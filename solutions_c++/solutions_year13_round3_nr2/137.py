#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}
const int N = 505;
int x, y;
string ans;
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t, cas = 1, i, j;
    cin >> t;
    while(t--)
    {
        cin >> x >> y;
        int len = abs(x) + abs(y);
        ans = "";
        for(i = 1; i <= abs(x); i++)
        {
            if(x < 0)
                ans += "EW";
            else
                ans += "WE";
        }
        for(i = 1; i <= abs(y); i++)
        {
            if(y < 0)
                ans += "NS";
            else
                ans += "SN";
        }
        cout << "Case #" << cas++ << ": " << ans << endl;
    }
    return 0;
}
