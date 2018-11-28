#include<stdio.h>

int main()
{
    int tc,t,x,r,c,pro;

    scanf("%d",&tc);
    for(t=0;t<tc;t++)
    {
        scanf("%d%d%d",&x,&r,&c);
        pro=r*c;
        printf("Case #%d: ",t+1);
        if(x==1)
            {
                printf("GABRIEL\n");
                continue;
            }
        if((pro%x==0)&&((x<=r)||(x<=c)))
           {
                if((r==1)||(c==1))
                    {
                        if(x>2)
                            {
                                printf("RICHARD\n");
                                continue;
                            }
                    }
                    printf("GABRIEL\n");
           }
        else
            printf("RICHARD\n");
    }
    return 0;
}
