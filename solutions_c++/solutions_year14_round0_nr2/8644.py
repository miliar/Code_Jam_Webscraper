#include <stdio.h>
#include <algorithm>

using namespace std;

double rec(double p,double c,double f, double x,int m)
{
    printf("%d %lf\n",m,p);
    return 1<<30;
    if(((c/p)+(x/(p+f)))>x/p)
        return x/p;
    return min((c/p)+rec(p+f,c,f,x,m+1),x/p);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int N;
    scanf("%d",&N);
    for(int I=1;I<=N;I++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double res=0;
        double p=2.0;
        while((((c/p)+(x/(p+f)))<x/p))
        {
            res+=c/p;
            p+=f;
        }
        res+=x/p;
        if(I>1)
        printf("\n");
        printf("Case #%d: %.7lf",I,res);
    }
    return 0;
}
