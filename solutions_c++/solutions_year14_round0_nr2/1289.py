#include<cstdio>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.in.txt","w",stdout);
    int TT,T;
    double c,f,x,sums,n;
    int y,i;
    scanf("%d",&TT);
    for (T=1;T<=TT;T++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        i=0;
        sums = x/2;
        while(1)
        {
            i++;
            n = x/(2+i*f)+c/(2+(i-1)*f)-x/(2+(i-1)*f);
            if (n>0)
                break;
            sums += n;
        }
        printf("Case #%d: %.7lf\n",T,sums);
    }
}
