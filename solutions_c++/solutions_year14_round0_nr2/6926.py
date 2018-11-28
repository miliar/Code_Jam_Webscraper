#include <iostream>
#include <cstdio>
#include <iomanip>
#include<cmath>
double farm(double,double,double);
using namespace std;

int main()
{   freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t;
    cin>>t;
    for(int t3=0;t3<t;t3++){
            double c,f,x,t1,t2,i=1;
            scanf("%lf%lf%lf",&c,&f,&x);
          //  printf("%lf  %lf  %lf\n",c,f,x);
            t1=x/2.0;
            t2 = (c/2.0)+(x/(2.0+f));
            while(t1>t2){
                i++;
                t1=t2;
                t2 = farm(c,i,f)+(x/(2.0+(f*i)));
            }
            printf("Case #%d: %.7f\n",t3+1,t1);
    }
    return 0;
}
double farm(double c,double i,double f){
    double ans=0;
    for(int k=0;k<i;k++){
        ans+=c/(2.0+(f*k));
    }
    return ans;
}
