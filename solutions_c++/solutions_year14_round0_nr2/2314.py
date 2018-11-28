#include<stdio.h>
#include<math.h>
#include<iostream>

#define EPSILON 0.000000000001

using namespace std;

int main(){
    int t,loopcheck,ccase=1;
    scanf("%d",&t);
    while(t--){
        double c,f,x,r,prevbeforeans,prevans,ans,n;
        scanf("%lf%lf%lf",&c,&f,&x);
        r=2.0;
        loopcheck=1;
        prevans=x/r;
        prevbeforeans=0.0;
        n=0;
        while(loopcheck){
            prevbeforeans=prevbeforeans+(c/(r+n*f));
            ans=prevbeforeans+(x/(r+(n+1)*f));
            if(ans-prevans>EPSILON && fabs(ans-prevans)>EPSILON)
                loopcheck=0;
            else
                prevans=ans;
            n+=1;
        }
        printf("Case #%d: %.7lf\n",ccase,prevans);
        ++ccase;
    }
    return 0;
}
