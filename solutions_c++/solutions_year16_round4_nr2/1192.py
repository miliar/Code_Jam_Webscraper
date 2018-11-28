#include <vector>
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <set>


using namespace std;

const int N=205;

double f[N][N][N];
int n,K;
double p[N];



double cal(vector<double> a)
{
    double ans=0;
    for(int i=0;i<(1<<K);i++)
    {
        double tmp=1;
        int sum=0;
        for(int j=0;j<K;j++)
        {
            if(i&(1<<j)) tmp*=a[j],sum++;
            else tmp*=(1-a[j]);
        }
        if(sum*2==K) ans+=tmp;
    }
    return ans;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        scanf("%d%d",&n,&K);
        for(int i=0;i<n;i++) scanf("%lf",p+i);

        double ans=0;
        for(int i=0;i<(1<<n);i++)
        {
            vector<double> a;
            for(int j=0;j<n;j++) if(i&(1<<j)) a.push_back(p[j]);
            if(a.size()==K)
            {
                ans=max(ans,cal(a));
            }
        }

        printf("%.9f\n",ans);
    }
}

