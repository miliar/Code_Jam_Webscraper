#include <iostream>
/*每天在CF上刷B,C，D题各一道*/
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
#define SIZE (2000+10)
#define Ri(a) scanf("%d", &a)
#define Rl(a) scanf("%I64d", &a)
#define Rf(a) scanf("%lf", &a)
#define Rs(a) scanf("%s", a)
#define Pi(a) printf("%d\n", (a))
#define Pf(a) printf("%lf\n", (a))
#define Pl(a) printf("%I64d\n", (a))
#define Ps(a) printf("%s\n", (a))
#define CLR(a, b) memset(a, (b), sizeof(a))
#define INT_MAX 2147483647
#define LL_MAX 9223372036854775807
#define ll __int64
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1
#define PI acos(-1.0)
const long long MOD = 1000000007;
using namespace std;

int main()
{
    freopen("D:b.in","r",stdin);
    freopen("D:b.out","w",stdout);
    int t,cas;
    string s;
    Ri(t);
    for(cas = 1; cas <= t; cas++)
    {
        getchar();
        cin>>s;
        int num = 0;
        if(s[0] == '-')
        {
            for(int i = 1; i < s.size(); i++)
            {
                if(s[i] != s[i-1])
                    num++;
            }
            if(num < 2)
                printf("Case #%d: %d\n",cas,1);
            else if(num%2 == 0)
                printf("Case #%d: %d\n",cas,num+1);
            else
                printf("Case #%d: %d\n",cas,num);
        }
        else
        {
            for(int i = 1; i < s.size(); i++)
            {
                if(s[i] != s[i-1])
                    num++;
            }
            if(num < 1)
                printf("Case #%d: %d\n",cas,0);
            else if(num%2 == 1)
                printf("Case #%d: %d\n",cas,num+1);
            else
                printf("Case #%d: %d\n",cas,num);
        }
    }
    return 0;
}
