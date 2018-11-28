#include<bits/stdc++.h>
using namespace std;


char maz[444][444];
int n,m;
bool tr(int i,int j,char c)
{
    int x=i,y=j,f=0;
    do
    {
        if(c=='v')x++;
        else if(c=='^')x--;
        else if(c=='>')y++;
        else y--;
        if(x<0||x>=n||y<0||y>=m)
        {
            f=1;
            break;
        }
    }while(maz[x][y]=='.');
    return f;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%s",maz[i]);
        int no=1,ans=0;
        for(int i=0;i<n&&no;i++)
            for(int j=0;j<m&&no;j++)
                if(maz[i][j]!='.')
                {
                    if(tr(i,j,maz[i][j])==1)
                    {
                        ans++;
                        if(tr(i,j,'>')==1&&tr(i,j,'<')==1&&tr(i,j,'v')==1&&tr(i,j,'^')==1)
                        {
                            no=0;
                            break;
                        }
                    }
                }
        printf("Case #%d: ",ti++);
        if(no==0)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
