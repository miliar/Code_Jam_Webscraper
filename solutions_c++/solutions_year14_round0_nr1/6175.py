#include <stdio.h>

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int z,zz;
    scanf("%d",&z);
    for(zz=1;zz<=z;zz++)
    {
        int chk[17]={0,},x,t,i,flag=0,dap=0;
        printf("Case #%d: ",zz);
        scanf("%d",&x);
        for(i=0;i<16;i++)
        {
            scanf("%d",&t);
            if(i>=(x-1)*4 && i<4*x)
            {
                chk[t]++;
            }
        }

        scanf("%d",&x);
        for(i=0;i<16;i++)
        {
            scanf("%d",&t);
            if(i>=(x-1)*4 && i<4*x)
            {
                chk[t]++;
            }
        }

        for(i=1;i<=16;i++)
        {
            if(chk[i]==2)
            {
                if(dap!=0)flag=2;
                else
                {
                    dap=i;
                    flag=1;
                }
            }
        }
        if(flag==2)puts("Bad magician!");
        else if(flag==0)puts("Volunteer cheated!");
        else printf("%d\n",dap);
    }
}
