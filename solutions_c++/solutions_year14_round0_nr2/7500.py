#include<cstdio>
#include<iostream>
#include<algorithm>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;

int a[20],b[6][6];

int main(){
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    int st;
    scanf("%d",&st);
    rep(xxx,st){
        printf("Case #%d: ",xxx+1);
        double c,f,x,time=0,r=2,kq=1000000000ll*1000000000;
        cin>>c>>f>>x;
        rep(i,1000000){
            double t=time+(x/r);
            if (t<kq) kq=t;
            time+=c/r;
            r+=f;
        }
        printf("%f\n",kq);
    }

}
