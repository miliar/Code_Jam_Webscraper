#include<stdio.h>
#include<algorithm>
int n,m;
struct cell
{
    int i,j;
    int h;
};
typedef struct cell cell;

cell sq[10000];
int lawn[101][101];
int res[101][101];
bool compare(cell a,cell b)
{
    if(a.h<b.h) return (bool)1;
    else return (bool)0;
}
int compare_row(int r,int h)
{
    for(int i=1;i<=m;i++)
    {
        if(lawn[r][i]>h) return 0;
    }
    for(int i=1;i<=m;i++)
    {
        if(lawn[r][i]==h) res[r][i]=1;
    }
    return 1;
}
int compare_col(int c,int h)
{
    for(int i=1;i<=n;i++)
    {
        if(lawn[i][c]>h) return 0;
    }
    for(int i=1;i<=n;i++)
    {
        if(lawn[i][c]==h) res[i][c]=1;
    }
    return 1;
}
int main()
{
    int t,count=0,l,x,y,status,flag=0,c=1;
    scanf("%d",&t);

    while(t--)
    {
        scanf("%d %d",&n,&m);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
                res[i][j]=0;
        }
        flag=0;count=0;
        for(int p=1;p<=n;p++)
        {
            for(int q=1;q<=m;q++)
            {
                scanf("%d",&lawn[p][q]);
                sq[count].h=lawn[p][q];
                sq[count].i=p;
                sq[count].j=q;
                count++;
            }
        }
        std::sort(sq,sq+count,compare);
        for(int p=0;p<count;p++)
        {
            x=sq[p].i;
            y=sq[p].j;
            if(res[x][y]==0)
            {
                l=sq[p].h;
                status=compare_row(sq[p].i,l);
                if(status==0)
                {
                    status=compare_col(sq[p].j,l);
                    if(status==0)
                    {
                        printf("Case #%d: NO\n",c);flag=1;
                        break;
                    }
                }
            }

        }
        if(flag==0)printf("Case #%d: YES\n",c);


        c++;
    }
    return 0;
}
