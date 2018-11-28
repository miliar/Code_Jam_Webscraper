#include <cstdio>

using namespace std;

int v[100],lover[100],mat[20][20];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<2*(n+m);i++) scanf("%d",&v[i]);
        for(int i=0;i<2*(n+m);i++)
            lover[v[i]]=v[i^1];
        int lim=1<<(n*m),gasit=0;
        for(int mask=0;mask<lim;mask++)
        {
            for(int i=0;i<n;i++)
                for(int j=0;j<m;j++)
                    if(mask&(1<<m*i+j)) mat[i][j]=1;
                    else mat[i][j]=0;
            int ok=1;
            for(int i=0;i<2*(n+m);i++)
            {
                int dir,x,y;
                if(i<m) {dir=0;x=0;y=i;}
                else if(i<n+m) {dir=1;x=i-m;y=m-1;}
                else if(i<n+2*m) {dir=2;x=n-1;y=m-(i-n-m)-1;}
                else {dir=3;x=n-(i-2*m-n)-1;y=0;}
                while(0<=x && x<n && 0<=y && y<m)
                {
                    if(mat[x][y]==0)
                    {
                        if(dir==0) {y--;dir=1;}
                        else if(dir==1) {x++;dir=0;}
                        else if(dir==2) {y++;dir=3;}
                        else if(dir==3) {x--;dir=2;}
                    }
                    else
                    {
                        if(dir==0) {y++;dir=3;}
                        else if(dir==1) {x--;dir=2;}
                        else if(dir==2) {y--;dir=1;}
                        else if(dir==3) {x++;dir=0;}
                    }
                }
                if(x==-1)
                {
                    if(lover[i+1]!=y+1) {ok=0;break;}
                }
                else if(y==m)
                {
                    if(lover[i+1]!=m+x+1) {ok=0;break;}
                }
                else if(x==n)
                {
                    if(lover[i+1]!=m+n+(m-y)) {ok=0;break;}
                }
                else if(y==-1)
                {
                    if(lover[i+1]!=m+n+m+(n-x)) {ok=0;break;}
                }
            }
            if(ok) {gasit=1;break;}
        }
        printf("Case #%d:\n",t);
        if(gasit)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<m;j++)
                    if(mat[i][j]==0) printf("/");
                    else printf("\\");
                printf("\n");
            }
        }
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
