#include<stdio.h>
int main()
{
    //freopen("date.in","r",stdin);
    //freopen("date.out","w",stdout);
    int t,nr=0;
    double sol,aux,timp,cur,c,f,x;

    scanf("%d",&t);
    while(t-- && ++nr)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        cur=2;timp=0;sol=(double)x/cur;

        while(true)
        {
            aux=(double)c/cur+(double)x/(cur+f);

            if(timp+aux<sol)
            {
                sol=timp+aux;
                timp+=(double)c/cur;
                cur+=f;
            }else
                break;
        }

        printf("Case #%d: %.7lf\n",nr,sol);
    }

    return 0;
}
