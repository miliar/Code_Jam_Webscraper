#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

double c,f,x,now,best;
double u1,u2;
int ca=0;

void work()
{
    scanf("%lf%lf%lf",&c,&f,&x);

    best=x/2;
    u1=0;
    for (int k=1;k<=50010;++k)
    {
        u2=u1+c/(2.0+(k-1)*f);u1=u2;
        now=u2+x/(2.0+k*f);
        if (now<best) best=now;
    }

    printf("Case #%d: %.7lf\n",++ca,best);
}

int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);

    int t;scanf("%d",&t);
    while (t--) work();

    fclose(stdin);
    fclose(stdout);
}
