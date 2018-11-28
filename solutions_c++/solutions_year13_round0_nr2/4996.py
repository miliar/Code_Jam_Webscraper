#include<stdio.h>
#include<string.h>
int grid[110][110];
int gen[110][110];
int n,m;
bool match()
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++) if(grid[i][j]!=gen[i][j])
            return false;
    return true;
}
void generate(int st1,int st2)
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            gen[i][j]=2;
    for(int i=0;i<n;i++) if((1<<i)&st1)
    {
        for(int j=0;j<m;j++)
            gen[i][j]=1;
    }
    for(int i=0;i<m;i++) if((1<<i)&st2)
    {
        for(int j=0;j<n;j++)
            gen[j][i]=1;
    }
}
void print()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
            printf("%d",gen[i][j]);
        printf("\n");
    }
}
int main()
{
    int T;
    int ca=0;
    //freopen("in.in","r",stdin);
   // freopen("b.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {

        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&grid[i][j]);
        int st1=(1<<n);
        int st2=(1<<m);
        int res=0;
        for(int i=0;i<st1;i++)
            for(int j=0;j<st2;j++)
            {
                generate(i,j);
                //printf("%d %d\n",i,j);

               // print();
                if(match())
                {
                    res=1;
                    break;
                }
            }
        if(res)
            printf("Case #%d: YES\n",++ca);
        else
            printf("Case #%d: NO\n",++ca);
    }
}
