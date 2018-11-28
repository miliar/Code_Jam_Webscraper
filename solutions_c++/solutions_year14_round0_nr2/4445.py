#include <iostream>
#include <cstdio>
using namespace std;

double timemy[1000000],made[1000000];
double C,F,X;

bool trybuy(int num)
{
    if (num==0)
    {
        made[num]=0;
        timemy[num] = X/2;
    }
    else {
        made[num] = made[num-1]+C/(F*(num-1)+2);
        timemy[num] = made[num]+X/(F*num+2);
    }


}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    int t,T,i,j;

    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        int k=0;
        for (i=0;i<=X;i++)
            trybuy(i);
        for (i=1;i<=X;i++)
        if (timemy[i]<timemy[k])
        {
            k=i;
        }

        printf("Case #%d: %.7f\n",t,timemy[k]);
    }
    return 0;
}
