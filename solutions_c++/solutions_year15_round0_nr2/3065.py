/**

¼ªÁÖ´óÑ§
Jilin U

Author:     sinianluoye (JLU_LiChuang)
Date:        2015-3
Usage:

**/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define ll long long
#define eps 1e-8
#define ms(x,y) (memset(x,y,sizeof(x)))
#define fr(i,x,y) for(int i=x;i<=y;i++)
#define sqr(x) ((x)*(x))

using namespace std;
const int maxn=1e3+10;
int a[maxn];
bool cmp(int a,int b)
{
    return a>b;
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    cin>>T;
    int cas=0;
    while(T--)
    {
        printf("Case #%d: ",++cas);
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n,cmp);
        int ans=0x3f3f3f3f;
        for(int i=1;i<=a[0];i++)
        {
            int t=i;
            for(int j=0;j<n;j++)
                t+=(a[j]-1)/i;
            ans=min(ans,t);
        }
        cout<<ans<<endl;
    }
}

/*************copyright by sinianluoye (JLU_LiChuang)***********/
