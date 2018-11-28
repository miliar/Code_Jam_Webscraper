#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstdlib>
#define N 60
using namespace std;
class num
{
    public:
    int x,y;
    num(int h,int w):x(h),y(w){}
};
int a[N][N],b[N][N];
bool status[N][N];
int X[]={0,0,1,-1,-1,-1,1,1};
int Y[]={-1,1,0,0,-1,1,-1,1};
int main()
{
    //freopen("C-small-attempt6.in","r",stdin);
    freopen("C-small-attempt6.out","w",stdout);
    int bfs(int n,int m);
    int t,T = 1;
    for(int n=1;n<=5;n++)
    {
        for(int m=1;m<=5;m++)
        {
           for(int wb=0;wb<n*m;wb++)
           {
        //int n,m,c;
        //scanf("%d %d %d",&n,&m,&c);
        int c = wb;
        printf("%d %d %d\n",n,m,c);
        if((n*m-c)==4&&n>=2&&m>=2)
        {
            printf("Case #%d:\n",T++);
            memset(a,0,sizeof(a));
            a[n][m] = 2;
            a[n-1][m] = 1;
            a[n][m-1] = 1;
            a[n-1][m-1] = 1;
            for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    if(a[i][j]==2)
                    {
                        printf("c");
                    }else if(a[i][j]==1)
                    {
                        printf("*");
                    }else
                    {
                        printf(".");
                    }
                }
                printf("\n");
            }
            continue;
        }
        int pre = c;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        //0 . 1 Õ¨µ¯ 2 Æðµã
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(c>0)
                {
                    a[i][j] = 1;
                    c--;
                }
                if(c==0)
                {
                    break;
                }
            }
            if(c==0)
            {
                break;
            }
        }
        //a[n][m] = 2;
        if((n*m-pre)/m==1&&n-1>=1)
        {
            for(int i=n-1;i<=n;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    a[i][j] = 0;
                }
            }
            int sum = pre%m;
            if(sum==0)
            {
                sum = m;
            }
            for(int i=1;i<=m;i++)
            {
                for(int j=n-1;j<=n;j++)
                {
                    if(sum>0)
                    {
                        a[j][i] = 1;
                        sum--;
                    }
                    if(sum==0)
                    {
                        break;
                    }
                }
                if(sum==0)
                {
                    break;
                }
            }
            sum = pre%m;
            if(sum==0)
            {
                sum = m;
            }
            int col = sum/2+1;
            if(sum%2==1&&col+1<=m&&m>=3&&n>2)
            {
                a[n][col] = 1; a[n-2][m] = 0;
                a[n-1][col+1] = 1; a[n-2][m-1] = 0;
                a[n][col+1] = 1; a[n-2][m-2] = 0;
            }
        }
        if((n*m-pre)/m==2&&pre%m==m-1&&m>3)
        {
            int row = pre/m+1;
            a[row+1][1] = 1;
            a[row+2][1] = 1;
            a[row][m-1] = 0;
            a[row][m-2] = 0;
        }
        if((n*m-pre)/m>2&&pre%m==m-1&&m>3)
        {
            int row = pre/m+1;
            a[row+1][1] = 1;
            a[row+1][2] = 1;
            a[row][m-1] = 0;
            a[row][m-2] = 0;
        }
        if((n*m-pre)/m>=1&&pre%m==m-1&&m==3)
        {
            int row = pre/m+1;
            a[row][m-1] = 0;
            a[row+1][1] = 1;
        }
         for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(a[i][j]==0)
                {
                    for(int u=0;u<=7;u++)
                    {
                        int x = i+X[u];
                        int y = j+Y[u];
                        if(x>=1&&x<=n&&y>=1&&y<=m&&a[x][y])
                        {
                            b[i][j] = 1;
                            break;
                        }
                    }
                }
            }
        }
        a[n][m] = 2;
        /*
        for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    if(a[i][j]==1)
                    {
                        printf("*");
                    }else if(a[i][j]==0)
                    {
                        printf(".");
                    }else
                    {
                        printf("c");
                    }
                }
                printf("\n");
            } */
        //cout<<"fa"<<endl;
        int k = bfs(n,m);
        //cout<<k<<endl;
        printf("Case #%d:\n",T++);
        if((n*m-pre!=1)&&k!=n*m-pre)
        {
            printf("Impossible\n");
        }else
        {
            for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    if(a[i][j]==1)
                    {
                        printf("*");
                    }else if(a[i][j]==0)
                    {
                        printf(".");
                    }else
                    {
                        printf("c");
                    }
                }
                printf("\n");
            }
        }
           }
        }

    }
    return 0;
}
int bfs(int n,int m)
{
    if(b[n][m])
    {
        return 0;
    }
    //cout<<n<<" "<<m<<endl;
    memset(status,false,sizeof(status));
    int x1 = n;
    int y1 = m;
    queue<num> que;
    que.push(num(x1,y1));
    status[x1][y1] = true;
    int s = 1;
    while(!que.empty())
    {
        num nu = que.front();
        que.pop();
        x1 = nu.x;
        y1 = nu.y;
        for(int i=0;i<=7;i++)
        {
            int x2 = x1+X[i];
            int y2 = y1+Y[i];
            if(x2>=1&&x2<=n&&y2>=1&&y2<=m&&a[x2][y2]==0&&!status[x2][y2])
            {
                s++;
                status[x2][y2] = true;
                if(!b[x2][y2])
                {
                    que.push(num(x2,y2));
                }
            }
        }
    }
    return s;
}
