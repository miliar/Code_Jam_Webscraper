#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
using namespace std;
#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

int n,x;
int s[10005];
void init()
{
    scanf("%d%d",&n,&x);
    for (int i=0;i<n;i++)
        scanf("%d",&s[i]);
    sort(s,s+n);
}

void solve()
{
    int a=0,b=n-1,ans=0;
    while (a<b)
    {
        if (s[a]+s[b]>x)
        {
            ans++,b--;
        }
        else
        {
            ans++,b--,a++;
        }
    }
    if (a==b)ans++;
    printf("%d\n",ans);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int Q;
    scanf("%d",&Q);
    for (int i=1;i<=Q;i++)
    {
        init();
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
