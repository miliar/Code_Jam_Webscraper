#include <bits/stdc++.h>

using namespace std;

const int MAXN = 110;

typedef pair<int,int> pii;

int A[MAXN][MAXN];
bool visited[MAXN][MAXN];

struct thang
{
    int x, y;
};

thang Q[MAXN*MAXN];

int di[4]={-1,1,0,0}, dj[4]={0,0,1,-1};
int M, N;

void nhap()
{
    scanf("%d%d\n",&M,&N);
    for(int i=1; i<=M; i++)
    {
        for(int j=1; j<=N; j++)
        {
            char c=getchar();
            if (c=='^')
                A[i][j]=0;
            else if (c=='v')
                A[i][j]=1;
            else if (c=='>')
                A[i][j]=2;
            else if (c=='<')
                A[i][j]=3;
            else A[i][j]=-2;
        }
        scanf("\n");
    }
}

thang make(int x, int y)
{
    thang t;
    t.x=x; t.y=y; return t;
}

bool ktr(int x, int y)
{
    return (x>=1&&y>=1&&x<=M&&y<=N);
}

pii ke(int x, int y)
{
    int dx = di[A[x][y]], dy = dj[A[x][y]];
    while (1)
    {
        x+=dx; y+=dy;
        if (!ktr(x,y)) return (make_pair(x,y));
        if (A[x][y]!=-2) return (make_pair(x,y));
    }
}

int bfs(int sx, int sy)
{
    int l=0, r=0;
    Q[0]=make(sx,sy);
    visited[sx][sy]=1;
    while (l<=r)
    {
        int x = Q[l].x, y = Q[l].y; l++;
        //cout<<x<<' '<<y<<' '<<visited[x][y]<<endl;
        pii t = ke(x,y);
        if (!ktr(t.first,t.second))
            break;
        //cout<<t.first<<' '<<t.second<<endl;
        if (visited[t.first][t.second]) return 0;
        visited[t.first][t.second]=1;
        Q[++r]=make(t.first,t.second);
    }
    l--;
    int t = A[Q[l].x][Q[l].y];
    for(int k=0; k<4; k++)
    if (k!=t)
    {
        A[Q[l].x][Q[l].y]=k;
        pii t = ke(Q[l].x,Q[l].y);
        if (ktr(t.first,t.second))
            return 1;
    }
    return -1;
}

int tinh()
{
    memset(visited,0,sizeof(visited));
    int res = 0;
    for(int i=1; i<=M; i++)
    {
        for(int j=1; j<=N; j++)
        if (A[i][j]!=-2&&(!visited[i][j]))
        {
            int t = bfs(i,j);
           // cout<<'a'<<t<<endl;
            if (t==-1) return -1;
            res+=t;
        }
    }
    return res;
}

int main()
{
    freopen("test.inp","r",stdin); freopen("test.out","w",stdout);
    int T; scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        nhap();
        int res = tinh();
        if (res!=-1)
            printf("Case #%d: %d\n",t,res);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
	return 0;
}
