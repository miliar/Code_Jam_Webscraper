#include<iostream>
#include<cstdio>
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,ca,c,ans,x,r;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
    {
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",ca);
        if(x==3)
        {
            if(r==1 && c==3 || r==3 && c==1)
            {
                printf("RICHARD\n");
                continue;
            }
            else if(((r*c)%x)==0)
            {
                printf("GABRIEL\n");
                continue;

            }
            else
            {
                printf("RICHARD\n");
                continue;
            }
        }
        else if(x==4)
        {
            if(r==4 && c==2 || r==2 && c==4 || r==4 && c==1 ||r==1 && c==4 ||r==2 && c==2)
            {
                printf("RICHARD\n");
                continue;
            }
            else if(((r*c)%x)==0)
            {
                printf("GABRIEL\n");
                continue;

            }
            else
            {
                printf("RICHARD\n");
                continue;
            }
        }
        else
        {
            if(((r*c)%x)==0)
            {
                printf("GABRIEL\n");
                continue;

            }
            else
            {
                printf("RICHARD\n");
                continue;
            }
        }
    }
    return 0;
}
