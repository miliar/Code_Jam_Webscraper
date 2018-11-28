#include<stdio.h>
int main()
{
    freopen("A1.in","r",stdin);
    freopen("A11.txt","w",stdout);
    int q,i,j,k,ox,oo,d,y;
    k=1;
    char a[5][5];
    scanf("%d",&q);
    while(q--)
    {
        for(i=0;i<4;i++)
            scanf("%s",a[i]);
        printf("Case #%d:",k++);
        y=0;
        d=0;
        for(i=0;i<4;i++)
        {
            ox=0;
            oo=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='X')ox++;
                if(a[i][j]=='O')oo++;
                if(a[i][j]=='.')d++;
                if(a[i][j]=='T')
                {
                    ox++;
                    oo++;
                }
            }
            if(ox==4)
            {
                printf(" X won\n");
                y=1;break;
            }
            if(oo==4)
            {
                printf(" O won\n");
                y=1;break;
            }
        }
        if(y==0)
        {
            for(j=0;j<4;j++)
            {
                ox=0;
                oo=0;
                for(i=0;i<4;i++)
                {
                    if(a[i][j]=='X')ox++;
                    if(a[i][j]=='O')oo++;
                    if(a[i][j]=='T')
                    {
                        ox++;
                        oo++;
                    }
                }
                if(ox==4)
                {
                    printf(" X won\n");
                    y=1;break;
                }
                if(oo==4)
                {
                    printf(" O won\n");
                    y=1;break;
                }
            }
        }
        if(y==0)
        {
            ox=0;
            oo=0;
            for(i=0;i<4;i++)
            {
                if(a[i][i]=='X')ox++;
                if(a[i][i]=='O')oo++;
                if(a[i][i]=='T')
                {
                    ox++;
                    oo++;
                }
                if(ox==4)
                {
                    printf(" X won\n");
                    y=1;break;
                }
                if(oo==4)
                {
                    printf(" O won\n");
                    y=1;break;
                }
            }
        }
        if(y==0)
        {
            ox=0;
            oo=0;
            for(i=3,j=0;i>=0;i--,j++)
            {
                if(a[i][j]=='X')ox++;
                if(a[i][j]=='O')oo++;
                if(a[i][j]=='T')
                {
                    ox++;
                    oo++;
                }
                if(ox==4)
                {
                    printf(" X won\n");
                    y=1;
                }
                if(oo==4)
                {
                    printf(" O won\n");
                    y=1;
                }
            }
        }
        if(y==0)
        {
            if(d!=0)
                printf(" Game has not completed\n");
            else printf(" Draw\n");
        }
    }
    return 0;
}
