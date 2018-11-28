#include <stdio.h>
#include <string.h>
int lawn [105][105];
int flag[105][105];
int n,m;

int isOK()
{
     for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(lawn[i][j]<lawn[i][104])
                    flag[i][j]++;
                if(flag[i][j]==2)
                    return 0;
            }
     for(int j=0;j<m;j++)
            for(int i=0;i<n;i++)
            {
                if(lawn[i][j]<lawn[104][j])
                    flag[i][j]++;
                if(flag[i][j]==2)
                    return 0;
            }
    return 1;

}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,t;
    scanf("%d",&T);
    t=T;
    while(T--)
    {
        memset(lawn,0, sizeof(int)*105*105);
        memset(flag,0, sizeof(int)*105*105);
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
        {
            int rmax=-1;
            for(int j=0;j<m;j++)
            {
                scanf("%d",&lawn[i][j]);
                if(lawn[i][j] > rmax)
                    rmax=lawn[i][j];
            }
            lawn[i][104]=rmax;
        }

        for(int j=0;j<m;j++)
        {
            int cmax=-1;
            for(int i=0;i<n;i++)
            {
                if(lawn[i][j] > cmax)
                    cmax=lawn[i][j];
            }
            lawn[104][j]=cmax;
        }

        int x=isOK();
        if(x==1)
            printf("Case #%d: YES\n",t-T);
        else
            printf("Case #%d: NO\n",t-T);
    }

    fclose(stdin);
	fclose(stdout);

    return 0;
}
