#include <stdio.h>
#include <string.h>

int map[111][111];

bool check(int i,int j,int n,int m)
{   int x,y;
    bool okn=true,oks=true,okw=true,oke=true;
    for(x=i,y=j;x>=0;--x)
        if(map[x][y]>map[i][j])
            okn=false;
    for(x=i,y=j;y>=0;--y)
        if(map[x][y]>map[i][j])
            okw=false;
    for(x=i,y=j;x<n;x++)
        if(map[x][y]>map[i][j])
            oks=false;
    for(x=i,y=j;y<m;++y)
        if(map[x][y]>map[i][j])
            oke=false;
    if((!okw||!oke)&&(!oks||!okn))
        return true;
    return false;
}

int main()
{
    int t,n,m,c=0;
    scanf("%d",&t);
    while(t--)
    {
        c++;
        bool ok=true;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
            scanf("%d",&map[i][j]);
            printf("Case #%d: ",c);
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
            if(check(i,j,n,m)&&ok)
            {
                ok=false;
                printf("NO\n");
            }
        if(ok)
            printf("YES\n");
    }
    return 0;
}
