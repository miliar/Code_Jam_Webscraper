#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
long long t,a,b;
long long p[1001],pal[1001];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%lld",&t);
    for(int i=1; i<=1000; i++)
    {
        int k=i,br=0,e=0;
        while(k>0) {p[++br]=k%10; k/=10;}
        for(int j=1; j<=br/2; j++) if(p[br-j+1]!=p[j]) {e=1; break;}
        if(e==0) pal[i]=1;
    }
    for(int o=1; o<=t; o++)
    {
        scanf("%lld%lld",&a,&b);
        int ans=0;
        for(int i=1; i*i<=b; i++)
        {
            if(pal[i]>0&&pal[i*i]>0&&i*i>=a) ans++;
        }
        printf("Case #%d: %d\n",o,ans);
    }
    return 0;
}
