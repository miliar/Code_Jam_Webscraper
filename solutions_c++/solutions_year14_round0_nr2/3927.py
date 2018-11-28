#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int cases,t=1;
    double c,f,x;
    scanf("%d",&cases);
    while(cases--){
        double total=0,m=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        /*c=500;
        f=4;
        x=2000;*/
        while(x/m>((c/m)+x/(m+f))){
              total = total + c/m;
                m=m+f;
           }
           total=total+x/m;

        printf("Case #%d: %.7lf\n",t,total);
        t++;
    }

return 0;
}

