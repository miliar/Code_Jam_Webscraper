#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <stack>
#include <string>
#include <map>
#include <assert.h>
#include <time.h>


#define abs(x) ((x)>=0?(x):-(x))
#define i64 long long
#define u32 unsigned int
#define u64 unsigned long long
#define clr(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define SZ(x) x.size()
#define PI acos(-1.0)
#define sqr(x) ((x)*(x))
#define MP(x,y) make_pair(x,y)
#define EPS 1e-8



#define pii pair<int,int>
#define FFF freopen("test","r",stdin)
#define all(a) a.begin(),a.end()

using namespace std;


void output(i64 x)
{
    if(x<0) putchar('-'),x=-x;
    if(x==0)
    {
        putchar('0');
        return;
    }
    int a[20],num=0;
    while(x) a[++num]=x%10,x/=10;
    while(num>0) putchar('0'+a[num--]);
}

inline i64 myInt()
{
    char c=getchar();
    while(!isdigit(c)&&c!='-') c=getchar();
    int flag=1;
    if(c=='-') flag=-1,c=getchar();
    i64 x=0;
    while(isdigit(c))
    {
        x=(x*10)+(c-'0');
        c=getchar();
    }
    if(-1==flag) return -x;
    return x;
}

const int INF=1e9;
const int mod=100007;
const int N=111;

char s[N][N];
int n,m;

int a[N],b[N];

int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

int ok(int x,int y)
{
    int d;
    if(s[x][y]=='^') d=0;
    else if(s[x][y]=='>') d=1;
    else if(s[x][y]=='v') d=2;
    else d=3;

    x+=dx[d];
    y+=dy[d];
    while(x>=1&&x<=n&&y>=1&&y<=m)
    {
        if(s[x][y]!='.') return 0;
        x+=dx[d];
        y+=dy[d];
    }
    return 1;
}

int cal()
{
    n=myInt();
    m=myInt();
    for(int i=1;i<=n;i++) scanf("%s",s[i]+1);
    clr(a,0);
    clr(b,0);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(s[i][j]!='.')
            {
                a[i]++;
                b[j]++;
            }
        }
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(s[i][j]!='.')
            {
                if(a[i]==1&&b[j]==1) return -1;
            }
        }
    }

    int ans=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(s[i][j]!='.')
            {
                if(ok(i,j)) ans++;
            }
        }
    }
    return ans;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);


    int T=myInt();
    int num=0;
    while(T--)
    {
        printf("Case #%d: ",++num);
        int ans=cal();
        if(ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}

