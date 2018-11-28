#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<cmath>
#include<queue>
#include<set>
using namespace std;
#define N 10010
#define LL long long
#define INF 0xfffffff
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = ~0u>>2;
int a[N];
int main()
{
    int t,x,n,i;
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    cin>>t;
    int kk = 0;
    while(t--)
    {
        cin>>n>>x;
        for(i = 1; i <= n; i++)
        scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        int k = 1;
        int ans = 0;
        for(i = n ;i >= 1; i--)
        {
            if(i==k)
            {
                ans++;
                break;
            }
            if(a[i]+a[k]<=x)
            {
                ans++;
                k++;
            }
            else ans++;
            if(k>=i) break;
        }
        printf("Case #%d: ",++kk);
        printf("%d\n",ans);
    }
    return 0;
}
