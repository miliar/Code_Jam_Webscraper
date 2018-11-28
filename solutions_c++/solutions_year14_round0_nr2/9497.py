#include <iostream>
#include <cstdio>

using namespace std;

double c,f,x;

double play(double r, double s){
    double a = x/r;
    double b = (c/r)+(x/(f+r));
    if(a<b)
        return s+a;
    else
        return play(r+f,s+(c/r));
}

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("a.out","w",stdout);
    int t = 0;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: %.7lf\n",i+1,play(2,0));
    }
    return 0;
}
