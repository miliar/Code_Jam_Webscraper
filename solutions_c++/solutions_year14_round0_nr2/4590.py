#include<cstdio>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    double c,f,x,all,i;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        all=i=0;
        while(all+x/(i*f+2.0)>all+c/(i*f+2.0)+x/(i*f+f+2.0))
        {
            all+=c/(i*f+2.0);
            i++;
        }
        printf("case #%d: %.10lf\n",I,all+x/(i*f+2.0));
    }
}
