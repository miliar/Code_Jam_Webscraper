#include<cstdio>
#include<algorithm>
#include<iostream>
#define N 10100
using namespace std;

typedef long long LL;

LL f[40010];

bool chpal(LL x){
    int a[20],i;
    a[0]=0;
    while(x){
        a[++a[0]]=x%10;
        x/=10;
    }
    for(i=1;i+i<=a[0];++i)if(a[i]!=a[a[0]-i+1])return false;
    return true;
}

int main(){
    int cas,tt=0,j,i,n,ix,iy;
    //puts("aa");
    //printf("%d\n",chpal(121));
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int a[20];
    LL x,y;
    f[n=1]=0;
    for(j=1;j<10000;++j){
        if(j%10==0)continue;
        x=j;
        a[0]=0;
        while(x){
            a[++a[0]]=x%10;
            x/=10;
        }
        for(x=0,i=1;i<a[0];++i)x=x*10+a[i];
        x=x*10+a[1];
        for(i=a[0];i>1;--i)x=x*10+a[i];
        y=x*x;
        if(chpal(y))f[++n]=y;
        for(x=0,i=1;i<=a[0];++i)x=x*10+a[i];
        for(i=a[0];i>=1;--i)x=x*10+a[i];
        y=x*x;
        if(chpal(y))f[++n]=y;
    }
    sort(f+1,f+n+1);
    //for(i=1;i<=n;++i)printf("%lld ",f[i]);
    scanf("%d",&cas);
    while(cas--){
        cin>>x>>y;
        ix=1;
        iy=n;
        while(f[ix]<x)++ix;
        while(f[iy]>y)--iy;
        printf("Case #%d: %d\n",++tt,iy-ix+1);
    }
    return 0;
}
