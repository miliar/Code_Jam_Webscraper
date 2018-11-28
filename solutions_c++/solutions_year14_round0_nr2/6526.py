#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    FILE *fp;
    long int i,j,t,k;
    double c,f,x,n,m,time,tm;
    fp=fopen("data","w");
    cin>>t;
    for(k=1;k<=t;k++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        time=0;
        n=2;
        m=x/n;
        time+=c/n;
        n+=f;
        tm=time;
        tm+=x/n;
        while(m>tm)
        {
            m=tm;
            time+=c/n;
            n+=f;
            tm=time;
            tm+=x/n;
        }
        printf("Case #%ld: %0.7lf\n",k,m);
        fprintf(fp,"Case #%ld: %0.7lf\n",k,m);
    }
    fclose(fp);
    return 0;
}
