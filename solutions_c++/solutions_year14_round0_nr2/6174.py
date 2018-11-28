#include <stdio.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int z,zz;
    scanf("%d",&z);
    for(zz=1;zz<=z;zz++)
    {
        printf("Case #%d: ",zz);
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        int n= (int)(x/c-2/f),i;
        if(n<0)n=0;
        double dap=0;
        for(i=0;i<n;i++)
        {
            dap = dap + c/(2+i*f);
        }
        dap = dap + x/(2+n*f);
        printf("%lf\n",dap);
    }
}
