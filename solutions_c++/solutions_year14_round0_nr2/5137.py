#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int l,t;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        double c,f,x,tim=0,d=2;
        scanf("%lf %lf %lf",&c,&f,&x);
        while((x/d)>(c/d)+(x/(d+f)))
        {
            tim+=c/d;
            d+=f;
        }
        tim+=x/d;
        printf("Case #%d: %.7lf\n",l,tim);
    }

    return 0;
}
