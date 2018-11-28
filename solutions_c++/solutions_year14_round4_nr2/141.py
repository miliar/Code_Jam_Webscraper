#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
using namespace std;
#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

struct S
{
    int a,id;
    bool operator< (const S& x)const{
        return a<x.a;
    }
}s[1005];
int n;

void init()
{
    scanf("%d",&n);

    for (int i=0;i<n;i++)
    {
        scanf("%d",&s[i].a);
        s[i].id=i;
    }
    sort(s,s+n);
}

void solve()
{
    int ans=0;
    int l=0,r=n-1;
    for (int k=0;k<n;k++)
    {
        //printf("%d\n",k);
        int dd=s[k].id;
        if (dd-l>r-dd)
        {
            ans+=r-dd;
            for (int j=k+1;j<n;j++)
            {
                if (s[j].id>dd)s[j].id--;
            }
            r--;
        }
        else
        {
            ans+=dd-l;
            for (int j=k+1;j<n;j++)
            {
                if (s[j].id<dd)s[j].id++;
            }
            l++;
        }
    }
    printf("%d\n",ans);
}
int main()
{
    freopen("B-large.in","r",stdin);
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
