#include <bits/stdc++.h>

#define rep(i,n) for(i=1;i<=n;i++)
#define Rep(i,n) for(i=0;i<n;i++)
#define For(i,a,b) for(i=a;i<=b;i++)

#define pb(x) push_back(x)
#define sz(x) x.size()

#define mem(ara,val) memset(ara,val,sizeof(ara))
#define eps 1e-9

#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define ss(ch) scanf("%s",ch)
#define pi(x) printf("%d",x)
#define pii(x,y) printf("%d %d",x,y)
#define piii(x,y,z) printf("%d %d %d",x,y,z)
#define pl(x) printf("%lld",x)
#define pll(x,y) printf("%lld %lld",x,y)
#define plll(x,y,z) printf("%lld %lld %lld",x,y,z)
#define ps(ch) printf("%s",ch)
#define Afridi 0
#define NL printf("\n")
#define SP printf(" ")
#define loj(x) printf("Case %d:",x)
#define Loj(x) printf("Case %lld:",x)
#define debug(str,x) cout << str << " " << x << endl;
#define Max 110
#define INF INT_MAX

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

LL dx[] = {+1,-1,+0,+0};
LL dy[] = {+0,+0,+1,-1};

LL dir(char c)
{
    if(c == '^')return 1;
    if(c == 'v')return 0;
    if(c == '<')return 3;
    if(c == '>')return 2;
}

LL tot,imp;
LL row[Max],col[Max];
bool visit[Max][Max];
char str[Max][Max];
LL r,c;

bool pos(LL x,LL y)
{
    if(0<= x && x< r && 0<= y && y < c)return 1;
    return 0;
}

void dfs(LL x,LL y,LL d,LL px,LL py)
{
    if(pos(x,y) == 0)
    {
        if(row[px] == 1 && col[py] == 1)imp = 1;
        tot++;
        return;
    }
    if(visit[x][y] && str[x][y]!='.')return;
    visit[x][y] = 1;
    LL my = d;
    if(str[x][y] != '.')
    {
        my = dir(str[x][y]);
        px = x;
        py = y;
    }
    dfs(x+dx[my],y+dy[my],my,px,py);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Alargeout.txt","w",stdout);

    LL t,T,x,y,i,j;
    sl(T);
    rep(t,T)
    {
        sll(r,c);
        Rep(i,r)ss(str[i]);
        mem(visit,0);
        mem(row,0);mem(col,0);
        Rep(i,r)
        {
            Rep(j,c)
            {
                if(str[i][j] != '.')
                {
                    row[i]++;
                    col[j]++;
                }
            }
        }
        LL ans = 0;
        imp = 0;
        Rep(i,r)
        {
            Rep(j,c)
            {
                if(visit[i][j] == 0 && str[i][j]!='.')
                {
                    tot = 0;
                    LL d = dir(str[i][j]);
                    dfs(i,j,d,i,j);
                    ans += tot;
                }
            }
        }
        if(imp == 0)printf("Case #%lld: %lld\n",t,ans);
        else printf("Case #%lld: IMPOSSIBLE\n",t);
    }

    return Afridi;
}
