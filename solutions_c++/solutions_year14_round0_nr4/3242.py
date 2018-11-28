#include<iostream>
#include<algorithm>
#include<cstdio>

#define eps 1e-10

#define maxn 1010

using namespace std;

int t,n,ans1,ans2;
double a[maxn],b[maxn];

int dcmp(double x)
{
    if (x<-eps) return -1;else return x>eps;
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    cin>>t;
    for (int cas=1;cas<=t;cas++)
    {
        cin>>n;
        for (int i=1;i<=n;i++) cin>>a[i];
        for (int i=1;i<=n;i++) cin>>b[i];
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        ans1=1;
        for (int i=1;i<=n;i++)
            if (dcmp(b[ans1]-a[i])<0) ans1++;

        ans2=n;
        for (int i=1;i<=n;i++)
            if (dcmp(a[n-ans2+1]-b[i])<0) ans2--;

        ans1--;
        printf("Case #%d: %d %d\n",cas,ans1,ans2);
    }
    return 0;
}


