#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <string>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define SIZE (200000+10)
#define Ri(a) scanf("%d", &a)
#define Rl(a) scanf("%I64d", &a)
#define Rf(a) scanf("%lf", &a)
#define Rs(a) scanf("%s", a)
#define Pi(a) printf("%d\n", (a))
#define Pf(a) printf("%lf\n", (a))
#define Pl(a) printf("%I64d\n", (a))
#define Ps(a) printf("%s\n", (a))
#define xx first
#define yy second
#define CLR(a, b) memset(a, (b), sizeof(a))
#define INT_MAX 2147483647
#define LL_MAX 9223372036854775807
#define ll __int64
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1
#define PI acos(-1.0)
const long long MOD = 1000000007;
using namespace std;
string str;
int k;
bool flip(int pos,int len)
{
    if(pos + k > len)
        return false;

    for(int i = 0; i < k; i++)
    {
        if(str[pos+i] == '-')
        {
            str[pos+i] = '+';
        }
        else
        {
            str[pos+i] = '-';
        }
    }
    return true;
}
int main()
{
 //   freopen("A.in","r",stdin);
 //   freopen("A.out","w",stdout);
    int t;
    Ri(t);
    for(int cas = 1; cas <= t; cas++)
    {
        int ans = 0;
        cin>>str>>k;
        int len = str.size();
        for(int i = 0; i < len; i++)
        {
            if(str[i] == '-')
            {
                if(flip(i,len))
                    ans++;
                else
                {
                    ans = -1;
                    break;
                }
            }
        }
        printf("Case #%d: ",cas);
        if(ans == -1)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n",ans);
        }
    }
    return 0;
}
