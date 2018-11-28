#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int a[1005];
bool cmp(int a, int b)
{
    return a>b;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int n;
        scanf("%d", &n);
        int maxn=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d", &a[i]);
            maxn=max(maxn, a[i]);
        }
        printf("Case #%d: ", ca++);
        sort(a, a+n, cmp);
        for(int i=1;i<=maxn;i++)
        {
            int num=0;
            for(int j=0;j<n;j++)
            {
                if(a[j]<=i)
                    break;
                num+=ceil(a[j]*1.0/i)-1;
            }
            maxn=min(maxn, num+i);
        }
        printf("%d\n", maxn);
    }
    return 0;
}
