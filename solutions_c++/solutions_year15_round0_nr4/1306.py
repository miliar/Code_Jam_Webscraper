#include<cstdio>
#include<cstdlib>
#include<cstring>

char S[1200];

int main(void)
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int cases;
    scanf("%d",&cases);

    int X,R,C;
    int i,j;

    for(i=1;i<=cases;i++)
    {
        int y = 1;
        scanf("%d %d %d",&X,&R,&C);
        if(X==1)
            y = 1;
        else if(X==2)
        {
            if(R%2==0||C%2==0)
                y = 1;
            else
                y = 0;
        }
        else if(X==3)
        {
            if((R==3&&C>=2)||(C==3&&R>=2))
                y = 1;
            else
                y = 0;
        }
        else
        {
            if(R<4&&C<4)
                y = 0;
            else
            {
                if(R==4&&C>2)
                    y = 1;
                else if(C==4&&R>2)
                    y = 1;
                else
                    y = 0;
            }

        }
        if((R*C)%X!=0)
            y = 0;
        if(y==1)
            printf("Case #%d: GABRIEL\n",i);
        else
            printf("Case #%d: RICHARD\n",i);

    }

    return 0;
}
