#include<iostream>
#include<cstdio>
#include<stdio.h>
using namespace std;

double c, f, x, s;
int judge()
{
    double temp = (c/s) + (x/(s+f));
    if(x/s > temp)
        return 1;
    else
        return 0;
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);

    int T,Case=1;
    scanf("%d",&T);
    while(T--){
        double tt = 0;
        s= 2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(judge()){
            tt += c/s;
            s += f;
        }
        tt += x/s;
        printf("Case #%d: %.7lf\n",Case++,tt);
    }
    return 0;
}
