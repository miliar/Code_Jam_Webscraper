#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<cmath>
#include<map>
#include<queue>
#define sqr(x)  ((x)*(x))
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int z=1; z<=t; z++)
    {
        double r,t;
        scanf("%lf %lf",&r,&t);
        //cout<<r<<" "<<t<<endl;
        double ans=floor((sqrt(sqr(4*r-2)+32*t)-(4*r-2))/8.0+1e-5);
        if((4*r+4*ans-2)*ans>2*t)ans--;
        printf("Case #%d: %.0lf\n",z,ans,(4*r+4*ans-2)*ans,2*t);
    }
}
