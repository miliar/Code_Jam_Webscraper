#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const double eps=1e-9;
double a[1010],b[1010];
int c[1010];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            cin>>a[i];
        for (int i=0;i<n;i++)
            cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        int ans1=0;
        memset(c,0,sizeof(c));
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                if (!c[j] && a[i]>b[j]+eps)
                {
                    c[j]=1;
                    ans1++;
                    break;
                }
        memset(c,0,sizeof(c));
        int ans2=n;
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                if (!c[j] && b[j]>a[i]+eps)
                {
                    c[j]=1;
                    ans2--;
                    break;
                }
        printf("Case #%d: %d %d\n",t,ans1,ans2);
    }
    return 0;
}
