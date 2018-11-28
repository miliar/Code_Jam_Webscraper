#include<cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,ii,i,j;
    char tb[4][5];
    bool x,o,empt;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        x=o=empt=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",tb[i]);
            for(j=0;j<4;j++)
            {
                if(tb[i][j]=='.')empt=1;
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(tb[i][j]=='X'||tb[i][j]=='T');
                else break;
            }
            if(j==4)x=1;
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(tb[j][i]=='X'||tb[j][i]=='T');
                else break;
            }
            if(j==4)x=1;
        }
        for(i=0;i<4;i++)
        {
            if(tb[i][i]=='X'||tb[i][i]=='T');
            else break;
        }
        if(i==4)x=1;
        for(i=0;i<4;i++)
        {
            if(tb[i][3-i]=='X'||tb[i][3-i]=='T');
            else break;
        }
        if(i==4)x=1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(tb[i][j]=='O'||tb[i][j]=='T');
                else break;
            }
            if(j==4)o=1;
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(tb[j][i]=='O'||tb[j][i]=='T');
                else break;
            }
            if(j==4)o=1;
        }
        for(i=0;i<4;i++)
        {
            if(tb[i][i]=='O'||tb[i][i]=='T');
            else break;
        }
        if(i==4)o=1;
        for(i=0;i<4;i++)
        {
            if(tb[i][3-i]=='O'||tb[i][3-i]=='T');
            else break;
        }
        if(i==4)o=1;
        printf("Case #%d: ",ii);
        if(x)
        {
            printf("X won\n");
        }
        else if(o)
        {
            printf("O won\n");
        }
        else if(empt)
        {
            printf("Game has not completed\n");
        }
        else
        {
            printf("Draw\n");
        }
    }
}
