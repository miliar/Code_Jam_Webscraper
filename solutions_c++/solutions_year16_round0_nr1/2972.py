#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair<PI, PI > PII;
const double eps=1e-5;
const int inf=1e5;
const LL mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e3+5;

bool vis[15];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int n;
//        for(n=1;n<=1000000;n++){
        scanf("%d", &n);
        printf("Case #%d: ", ca++);
        memset(vis, 0, sizeof(vis));
        bool flag=0;
        LL i;
        for(i=1;;i++)
        {
            LL tmp=n*1LL*i;
            while(tmp)
                vis[tmp%10]=1, tmp/=10;
            int j;
            for(j=0;j<10;j++)
                if(!vis[j])
                    break;
            if(j==10)
                break;
            if(i>=10000)
            {
                flag=1;
                break;
            }
        }
        if(flag)
            puts("INSOMNIA");
        else
            printf("%I64d\n", i*1LL*n);
//        }
    }
    return 0;
}

