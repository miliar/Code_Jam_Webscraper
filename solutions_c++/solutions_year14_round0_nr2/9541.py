
#include<cstdio>
#include<cmath>
#define eps 1e-9
double c,f,x;
//int id;
double dfs(double now,double lim)
{   //printf("%lf %lf\n",now,lim);
    //id++;
    if (x/now>lim) return x/now;
    if (f*x<c*(now+f)) return x/now;
   // if (fabs(x/now)<eps) return x/now;
    double re,tmp;
    re=x/now;
    tmp=c/now+dfs(now+f,lim-c/now);
    if (tmp<re) re=tmp;
    return re;
}
void doit()
{   //id=0;
    scanf("%lf%lf%lf",&c,&f,&x);
    printf("%.7lf\n",dfs(2,x/2));

}
int main()
{   freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
        {
            printf("Case #%d: ",++i);
            doit();
        }
}
