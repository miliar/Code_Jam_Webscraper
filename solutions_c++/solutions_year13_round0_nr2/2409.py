#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN=102;
int a[MAXN][MAXN];
int left[MAXN][MAXN],right[MAXN][MAXN];
int top[MAXN][MAXN],down[MAXN][MAXN];

int max(int x,int y)
{
    return (x>y)?x:y;
}
int main()
{
    int T,N,M;
    freopen("B-large.in","r",stdin);
    freopen("B_output_large.txt","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%d%d",&N,&M);
        memset(left,0,sizeof(left));
        memset(right,0,sizeof(right));
        memset(top,0,sizeof(top));
        memset(down,0,sizeof(down));
        for (int i=1;i<=N;i++)
        {
            for (int j=1;j<=M;j++)
            {
                scanf("%d",&a[i][j]);
                left[i][j]=max(a[i][j],left[i][j-1]);
                top[i][j]=max(a[i][j],top[i-1][j]);
            }
        }
        for (int i=N;i>0;i--)
        {
            for (int j=M;j>0;j--)
            {
                right[i][j]=max(a[i][j],right[i][j+1]);
                down[i][j]=max(a[i][j],down[i+1][j]);
            }
        }
        bool valid=true;
        for (int i=1;i<=N;i++)
        {
            for (int j=1;j<=M;j++)
            {
                if ((left[i][j]>a[i][j] || right[i][j]>a[i][j])
                   && (top[i][j]>a[i][j] || down[i][j]>a[i][j]))
                {
                    valid=false; break;
                }
            }
            if (!valid) break; 
        }
        printf("Case #%d: ",cases);
        if (valid) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
