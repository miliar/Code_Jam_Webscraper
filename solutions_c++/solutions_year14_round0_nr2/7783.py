#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for(int caseno=1; caseno<=t; caseno++)
    {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);

        double nowr=2, ans=0;

        while(X/(nowr+F) + C/nowr  < X/nowr)
        {
            ans += C/nowr;
            nowr += F;
        }
        ans += X/nowr;



        printf("Case #%d: %.7lf\n",caseno, ans);
    }


    return 0;
}



