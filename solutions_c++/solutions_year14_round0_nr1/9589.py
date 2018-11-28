#include <stdio.h>
int maze1[10][10],maze2[10][10];
int main()
{
    int t,i,j,ans,co,x,y,a,b,c,d,r1,r2,cs=1;
    //freopen("A-small-attempt2.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&r1);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++) scanf("%d",&maze1[i][j]);
        }
        scanf("%d",&r2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++) scanf("%d",&maze2[i][j]);
        }

        co=0;

        a=maze1[r1][1];
        b=maze1[r1][2];
        c=maze1[r1][3];
        d=maze1[r1][4];
        for(i=1;i<=4;i++)
        {
            if(maze2[r2][i]==a)
            {
                ans=a;
                co++;
            }
            else if(maze2[r2][i]==b)
            {
                ans=b;
                co++;
            }
            else if(maze2[r2][i]==c)
            {
                ans=c;
                co++;
            }
            else if(maze2[r2][i]==d)
            {
                ans=d;
                co++;
            }
        }
        printf("Case #%d: ",cs++);
        if(co==0) printf("Volunteer cheated!\n");
        else if(co==1) printf("%d\n",ans);
        else printf("Bad magician!\n");

    }
    return 0;
}
