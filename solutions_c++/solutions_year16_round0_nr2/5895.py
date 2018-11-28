#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cmath>
//#include <unordered_map>
//#define lson x<<1
//#define rson x<<1|1
//#define mid ((lt[x].l+lt[x].r)/2)
//#define ID(x, y) ((x)*m+(y))
//#define CHECK(x, y) ((x)>=0 && (x)<n && (y)>=0 && (y)<m)
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
const int INF=0x3f3f3f3f;
void Open()
{
    #ifndef ONLINE_JUDGE
        freopen("C:/Users/qingp/Downloads/B-large.in", "r",stdin);
        freopen("B-large.out","w",stdout);
    #endif // ONLINE_JUDGE
}
char str[1111];
char f[1111];
int main()
{
//    Open();
    f['-'] = '+', f['+'] = '-';
    LL T;
    scanf("%I64d", &T);
    LL cas = 0;
    while(T--)
    {
        cas++;
        scanf("%s", str);
        LL len = strlen(str);
        LL ans = 0;
        for(LL i = len-1; i >= 0; i--)
        {
            if(str[i] == '+') continue;
            if(i == 0) ans++;
            else
            {
                if(str[0] == '-')
                {
                    reverse(str, str+i+1);
                    for(LL j = 0; j < i + 1; j++) str[j] = f[str[j]];
                    ans++;
                }
                else
                {
                    LL idx = 0;
                    while(str[idx] == '+') idx++;
                    reverse(str, str+idx);
                    for(LL j = 0; j < idx; j++) str[j] = f[str[j]];
                    ans++;

                    reverse(str, str+i+1);
                    for(LL j = 0; j < i+1; j++) str[j] = f[str[j]];
                    ans++;
                }
            }
        }
        printf("Case #%I64d: %I64d\n", cas, ans);
    }
    return 0;
}
