#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
#define LL unsigned long long

const double eps=1e-8;

const int N=111,INF=0x3f3f3f3f;

int G[4][4],a[5],b[5];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("yy.out","w",stdout);
    int T;cin>>T;
    double C,F,X;
    for(int cs=1;cs<=T;++cs)
    {
        cin>>C>>F>>X;
        int n=max(0.0,floor(X/C-2/F-eps));
        double sum=0;
        for(int i=0;i<n;++i)
        {
            sum+=C/(2+i*F);
        }
        sum+=X/(2+n*F);
        printf("Case #%d: %.7f\n",cs,sum);
    }
    return 0;
}
