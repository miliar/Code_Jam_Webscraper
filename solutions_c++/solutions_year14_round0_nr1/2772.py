#include<stdio.h>
#include<string.h>

int a,b,s[4][4],t[4][4];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    for (int cnt=1;cnt<=amm;cnt++)
    {
        scanf("%d",&a);
        for (int i=0;i<4;i++)for (int j=0;j<4;j++)scanf("%d",&s[i][j]);
        scanf("%d",&b);a--,b--;
        for (int i=0;i<4;i++)for (int j=0;j<4;j++)scanf("%d",&t[i][j]);
        int ct=0,ans;
        for (int i=0;i<4;i++)for (int j=0;j<4;j++)if (s[a][i]==t[b][j])ct++,ans=s[a][i];
        printf("Case #%d: ",cnt);
        if (ct==0)printf("Volunteer cheated!\n");
        else if (ct==1)printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
