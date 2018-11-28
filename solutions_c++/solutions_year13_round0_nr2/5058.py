#include<stdio.h>
#include<string.h>
int map[101][101];
int max_h[101];
int  max_l[101];
int main()
{
    int t,i,j,z,n,m,flag,Max_H,Max_L;
    freopen("B-large.in", "r", stdin);
    freopen("Lawnmower.txt", "w", stdout);
    scanf("%d",&t);z = t;
    while(t--)
    {
        memset(map,0,sizeof(map));
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0,Max_H = 0;j<m;j++)
            {
                scanf("%d",&map[i][j]);
                if(Max_H<map[i][j]){Max_H = map[i][j];}
            }
            max_h[i] = Max_H;
        }
        for(i=0;i<m;i++)
        {
            for(j=0,Max_L = 0;j<n;j++)
            {
                if(Max_L<map[j][i]){Max_L = map[j][i];}
            }
            max_l[i] = Max_L;
        }
        flag = 0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(map[i][j]<max_l[j]&&map[i][j]<max_h[i])
                {
                    flag = 1;
                }
            }
            if(flag == 1)break;
        }

        if(flag == 1)
            printf("Case #%d: NO\n",z-t);
        else
            printf("Case #%d: YES\n",z-t);
    }
    return 0;
}
