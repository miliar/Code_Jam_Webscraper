#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <functional>
#include <numeric>
#include <sstream>
#include <stack>
#include <map>
#include <queue>

#define CL(arr, val)    memset(arr, val, sizeof(arr))

#define lc l,m,rt<<1
#define rc m + 1,r,rt<<1|1

#define ll __int64
#define L(x)    (x) << 1
#define R(x)    (x) << 1 | 1
#define MID(l, r)   (l + r) >> 1
#define Min(x, y)   (x) < (y) ? (x) : (y)
#define Max(x, y)   (x) < (y) ? (y) : (x)
#define E(x)        (1 << (x))
#define iabs(x)     (x) < 0 ? -(x) : (x)
#define OUT(x)  printf("%I64d\n", x)
#define lowbit(x)   (x)&(-x)
#define Read()  freopen("A-small-attempt1.in", "r", stdin)
#define Write() freopen("dout.txt", "w", stdout);


#define M 137
#define N 100005

using namespace std;


const int inf = 0x7f7f7f7f;
const int mod = 1000000007;

double pi = acos(-1.0);
ll sum;
ll r;
double t;

int main()
{
    Read();
    Write();
    int T;
    int cas = 1;
    scanf("%d",&T);
    while (T--)
    {
        cin>>r>>t;
        ll a1 = (r + 1)*(r + 1) - r*r;
        ll l = 1;
        ll r = (ll)t;
        ll ans = 0;
        while (l <= r)
        {
            ll mid = (l + r)/2;
            if ((1.0*mid*a1 + 2.0*mid*(mid - 1)) > t)
            {
                r = mid - 1;
            }
            else
            {

                l = mid + 1;
                ans = mid;
            }
        }
        cout<<"Case #"<<cas++<<": "<<ans<<endl;
    }
}
