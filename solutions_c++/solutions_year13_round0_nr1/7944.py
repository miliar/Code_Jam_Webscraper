#include<stdio.h>
int main()
{
    freopen("A0.in","r",stdin);
    freopen("A00.txt","w",stdout);
    int T,i,j,nx,num=1,no;
    char a[5][5];
    scanf("%d",&T);
    while(T--)
    {
        int yes=0,n=0;
        for(i=0;i<4;i++)
            scanf("%s",a[i]);
        for(i=0;i<4;i++)
        {
            nx=0;no=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='X') nx++;
                if(a[i][j]=='O') no++;
                if(a[i][j]=='T'){nx++;no++;}
                if(a[i][j]=='.') n++;
            }
            if(nx==4)
            {
                printf("Case #%d: X won\n",num++);
                yes=1;break;
            }
            if(no==4)
            {
                printf("Case #%d: O won\n",num++);
                yes=1;break;
            }
        }
        if(yes) continue;
        for(i=0;i<4;i++)
        {
            nx=0;no=0;
            for(j=0;j<4;j++)
            {
                if(a[j][i]=='X') nx++;
                if(a[j][i]=='O') no++;
                if(a[j][i]=='T'){nx++;no++;}
            }
            if(nx==4)
            {
                printf("Case #%d: X won\n",num++);
                yes=1;break;
            }
            if(no==4)
            {
                printf("Case #%d: O won\n",num++);
                yes=1;break;
            }
        }
        if(yes) continue;
        for(i=0,j=0,nx=0,no=0;i<4,j<4;i++,j++)
        {
            if(a[i][j]=='X') nx++;
            if(a[i][j]=='O') no++;
            if(a[i][j]=='T'){nx++;no++;}
        }
        if(nx==4)
        {
            printf("Case #%d: X won\n",num++);
            continue;
        }
        if(no==4)
        {
            printf("Case #%d: O won\n",num++);
            continue;
        }
        for(i=3,j=0,nx=0,no=0;i>=0,j<4;i--,j++)
        {
            if(a[i][j]=='X') nx++;
            if(a[i][j]=='O') no++;
            if(a[i][j]=='T'){nx++;no++;}
        }
        if(nx==4)
        {
            printf("Case #%d: X won\n",num++);
            continue;
        }
        if(no==4)
        {
            printf("Case #%d: O won\n",num++);
            continue;
        }
        if(n!=0) printf("Case #%d: Game has not completed\n",num++);
        else printf("Case #%d: Draw\n",num++);
    }
    return 0;
}
