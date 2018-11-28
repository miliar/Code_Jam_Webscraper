#include<stdio.h>

int main()
{
    freopen("BL.in","r",stdin);
    freopen("outBl.txt","w",stdout);
    int n;
    double c,f,x,tr,tu,p,k;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        p=2;
        tr=x/p;
        k=0;
        do
        {
            tu=k+c/p;
            p+=f;
            k=tu;
            tu+=x/p;
            if(tr>=tu)
            {
                tr=tu;
            }
            else    break;
        }while(true);
        printf("Case #%d: %.7lf\n",i,tr);
    }
    return 0;
}
