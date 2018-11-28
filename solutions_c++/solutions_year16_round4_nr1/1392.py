#include <cstdio>
#include <iostream>
#include <bitset>
#include <vector>
#include <cstring>
#include <queue>
#include <algorithm>
#define ls rt << 1
#define rs rt << 1 | 1
#define lson  rt << 1 , l , mid
#define rson rt << 1 | 1 , mid + 1 , r
using namespace std;
typedef long long ll;
const int maxn = 5555;

struct Node
{
    int x;
    char id;
} node[4];

bool cmp(Node a, Node b)
{
    return a.x < b.x;
}

int AA[3][maxn],now[3],s[3],Now,n,m;

bool P[3];

bool ok(int x,int y)
{
    if (y==-1) return 1;
    for (int i=1; i<=(1<<n); i++)
    {
        if (AA[x][i] < AA[y][i]) return 1;
        if (AA[x][i] < AA[y][i]) return 0;
    }
    return 1;
}

int Fail(int x)
{
    if (!x) return 1;
    if (x==1) return 2;
    if (x==2) return 0;
    return -1;
}

bool ok(int l,int mid,int r)
{
    int ll=mid-l+1;
    for (int i=1; i<=ll; i++)
    {
        if (AA[Now][l+i-1] > AA[Now][mid+i]) return 1;
        if (AA[Now][l+i-1] < AA[Now][mid+i]) return 0;
    }
    return 0;
}

void cc(int l,int r,int x,int len)
{
    if (!len)
    {
        AA[Now][l]=x;
        return;
    }
    int y=Fail(x);
    int mid=(l+r)>>1;
    cc(l,mid, x, len-1);
    cc(mid + 1,r, y, len-1);
    if (ok(l,mid,r))
        for (int i=l; i<=mid; i++)
            swap(AA[Now][i],AA[Now][i + (1<<(len-1))]);
}

bool sum()
{
    for (int i=1; i<=m; i++) now[AA[Now][i]]++;
    for (int i=0; i<3; i++)
        if (now[i] != s[i]) return 0;
    return 1;
}
char ans[maxn];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    int k = 0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d %d %d",&n,&s[1],&s[0],&s[2]);
        m = 1<<n;
        for (int i=0; i<3; i++)
        {
            P[i]=0;
            now[0]=now[1]=now[2]=0;
            Now=i;
            cc(1,m,i,n);
            if (sum())
				P[i] = 1;
        }
        int flag = -2;
        for (int i = 0; i < 3; ++i)
            if (P[i] && ok(i, flag)) flag = i;
        if (flag == -2)
			printf("Case #%d: IMPOSSIBLE\n",++k);
        else
        {
            memset(ans,0,sizeof(ans));
            for (int i = 1; i <= (1<<n); i++)
            {
                if (AA[flag][i]==0) ans[i]='P';
                if (AA[flag][i]==1) ans[i]='R';
                if (AA[flag][i]==2) ans[i]='S';
            }
            printf("Case #%d: %s\n",++k,ans+1);
        }
    }
    return 0;
}
