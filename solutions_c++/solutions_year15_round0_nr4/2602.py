#include<cstdio>
using namespace std;
int main()
{
    int t,x,r,c;
    scanf("%d",&t);
    for(int j=1; j<=t; j++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(r<c)
        {
            r=r^c;
            c=r^c;
            r=r^c;
        }
        if(x==1)
            printf("Case #%d: GABRIEL\n",j);
        else if(x==2)
        {
            if((r*c)%x==0)
                printf("Case #%d: GABRIEL\n",j);
            else
                printf("Case #%d: RICHARD\n",j);
        }
        else if(x==3)
        {

            if(r==1||r==2)
            {
                printf("Case #%d: RICHARD\n",j);
            }
            else if(r==3)
            {
                if(c==1)
                    printf("Case #%d: RICHARD\n",j);
                if(c==2||c==3)
                    printf("Case #%d: GABRIEL\n",j);
            }
            else
            {
                if(c==1||c==2||c==4)
                    printf("Case #%d: RICHARD\n",j);
                else
                    printf("Case #%d: GABRIEL\n",j);


            }

        }
        else
        {
            if(r==1||r==2||r==3)
                printf("Case #%d: RICHARD\n",j);
            else
            {
                if(c==1||c==2)
                    printf("Case #%d: RICHARD\n",j);
                else
                    printf("Case #%d: GABRIEL\n",j);

            }

        }

    }
    return 0;
}
