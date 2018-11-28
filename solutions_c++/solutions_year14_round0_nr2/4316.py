#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,t=0;cin>>T;
    double eps=1e-6;
    while (T--) {
        t++;printf("Case #%d: ",t);
        double C,F,X;
        scanf("%lf %lf %lf",&C,&F,&X);
        double t0=X/2;
        int k=floor(X/C-2.0/F);
        if (k<1) {printf("%.7lf\n",t0);continue;}
        double tk=X/(F*k+2.0);
        for (int i=0;i<k;i++) tk+=C/(2.0+F*i);
        if (tk+eps<t0) printf("%.7lf\n",tk);
        else printf("%.7lf\n",t0);
    }
    return 0;        
}
