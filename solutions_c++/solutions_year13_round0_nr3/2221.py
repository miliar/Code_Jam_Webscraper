#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;
int a[1000000],n;

bool check(int p)
{
    int y=p,q=0;
    int t[20];
    while (y) {t[++q]=y%10; y/=10;}
    for (int i=1; i<=q; i++) if (t[i]!=t[q+1-i]) return false;
    long long x=p; x*=p;
    int m=0,i;
    while (x) {t[++m]=x%10; x/=10;}
    for (i=1; i<=m; i++) if (t[i]!=t[m+1-i]) return false;
    return true;
}

void init()
{
    for (int i=1; i<=10000000; i++)
     if (check(i)) a[++n]=i;
}

int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("c.out","w",stdout);
    init();
    //cout<<n<<endl;
    int o,cas=0,i;
    long long l,r;
    scanf("%d",&o);
    while (o--)
    {
        cin>>l>>r;
        int ans=0;
        for (i=1; i<=n; i++)
        {
            long long x=(long long )a[i]*(long long )a[i];
            if (x>=l && x<=r) ans++;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}
