#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

double c,f,x;
int t;
int ca=1;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int i,j;
    double total,mi,p,te;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        total=0;
        p=2.0;
        mi=(double)x/2;
        while(total<mi)
        {
            te=total+(double)x/p;
            mi=min(mi,te);
            total+=(double)c/p;
            p+=f;
        }
        printf("Case #%d: %.7f\n",ca++,mi);
    }
    return 0;
}
