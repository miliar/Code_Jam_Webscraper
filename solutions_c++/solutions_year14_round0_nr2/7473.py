#include<stdio.h>
double F,c,f,x,d[100001],ans,sum,k;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,q,t,n;
    scanf("%d",&t);
    for(q=1;q<=t;q++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        F=0;
        for(i=0;i<=100000;i++)
        {
            d[i]=c/(F+2);
            F+=f;
            }
        ans=x/2;
        sum=ans;
        n=1;
        k=0;
        while(ans>=sum)
        {
            ans=sum;
            k+=d[n-1];
            sum=k+x/(n*f+2);
            n++;
            }
        printf("Case #%d: %lf\n",q,ans);
        }
    scanf(" ");
    }
