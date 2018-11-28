#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include<algorithm>
using namespace std;
#define maxn 105
int n;
double V,X;
struct xx{
    double r,c;
}z[maxn];
bool cmp(xx a,xx b){
    return a.c>b.c;
}
/*
 4
 2 99.999500 26.546400
 0.000100 26.509700
 99.999900 57.392500
 */
#define eps 1e-9
int main(){
    freopen("/Users/ZZ/Desktop/in.txt","r",stdin);
    freopen("/Users/ZZ/Desktop/out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cas=1;
    while (t--) {
        printf("Case #%d: ",cas++);
        double mmax=0;
        double mmin=10000000;
        scanf("%d%lf%lf",&n,&V,&X);
        // printf("%d %lf% lf\n",n,V,X);
        for(int i=0;i<n;i++){
            scanf("%lf%lf",&z[i].r,&z[i].c);
            //printf("%lf %lf\n",z[i].r,z[i].c);
            mmax=max(mmax,z[i].c);
            mmin=min(mmin,z[i].c);
        }
        sort(z, z+n, cmp);
        if(mmax<X-eps||mmin>X+eps){
            puts("IMPOSSIBLE");
            continue;
        }
        if(n==2)
        {
            double ans;
            double k0=(z[0].r*(z[0].c-X)),k1=(z[1].r*(X-z[1].c));
            if(k0<eps&&k1<eps)
            {
                ans=V/(z[0].r+z[1].r);
            }
            else if(k0<eps)
            {
                ans=V/(z[0].r);
            }
            else if(k1<eps)
            {
                ans=V/(z[1].r);
            }
            else
            {
                double s1=V/(k1/k0*z[0].r+z[1].r);
                ans=max(s1,s1*k1/k0);
            }
            printf("%.12f\n",ans);
        }
        else if(n==1)
        {
            double ans=V/z[0].r;
            printf("%.12f\n",ans);
        }
        //printf("%.12f\n",st);
    }
}