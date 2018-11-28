#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double A[100010];
        A[0]=X/2.0;
        A[1]=C/2.0 + X/(F+2.0);
        for(int i=2;i<100000;++i) A[i]=A[i-1]-X/(2.0+(i-1)*F)+X/(2.0+i*F)+C/(2.0+(i-1)*F);
        double res=*min_element(A,A+100000);
        printf("Case #%d: %.7lf\n",++cases,res);
    }
    return 0;
}
