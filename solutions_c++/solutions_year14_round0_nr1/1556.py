#include<stdio.h>
int main()
{
    int T;
    int f[5][5];
    int s[5][5];
    int ans;
    int res;
    int ca=1;
    freopen("A-small-attempt0.in","r",stdin);
    scanf("%d",&T);
    while(T--)
    {
        int first;
        int second;
        scanf("%d",&first);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                scanf("%d",&f[i][j]);
        }
        scanf("%d",&second);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                scanf("%d",&s[i][j]);
        }
        ans=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++) if(f[first-1][i]==s[second-1][j])
            {
                ans++;
                res=f[first-1][i];
            }
        }
        printf("Case #%d: ",ca++);
        if(!ans)
        {
            printf("Volunteer cheated!\n");
        }
        else if(ans==1)
        {
            printf("%d\n",res);
        }
        else
        {
            printf("Bad magician!\n");
        }

    }
}
