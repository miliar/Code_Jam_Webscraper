#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <cmath>
#define N 105
#define INF 0x6f6f6f6f
#define debug(a) cout<<#a<<' '<<a<<endl;
typedef long long LL;
using namespace std;
int mat[N][N];
int row[N],col[N];
struct node
{
    int x,y,w;
    friend bool operator<(node a,node b)
    {
        return a.w<b.w;
    }
}a[N*N];
int l;

bool check(int x,int y,int w)
{
    if(row[x]<=w)return true;
    if(col[y]<=w)return true;
    return false;
}


const char *solve()
{
    sort(a,a+l);

    for(int i=0;i<l;i++)
    {
        if(check(a[i].x,a[i].y,a[i].w)==false)return "NO";
    }
    return "YES";
}

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    int T,cas=1,n,m;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&n,&m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                scanf("%d",&mat[i][j]);
        memset(row,0,sizeof(row));
        memset(col,0,sizeof(col));
        l=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                row[i]=max(row[i],mat[i][j]);
                col[j]=max(col[j],mat[i][j]);
                a[l].x=i;
                a[l].y=j;
                a[l++].w=mat[i][j];
            }
        printf("Case #%d: %s\n",cas++,solve());
    }
	return 0;
}
