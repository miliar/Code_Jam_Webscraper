#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<sstream>
#include<string>
#include<bitset>
#include<utility>
#include<numeric>
#include<assert.h>

using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define repn(i,a,n) for (int i=a;i<=n;i++)

typedef long long LL;
typedef unsigned long long ULL;

const LL LINF = (1LL <<60);
const int INF = 0x3f3f3f3f;

const int NS = 3000;
const int MS = 55;
const int MOD = 1000000007;
const double PI = acos(-1.0);

#define form(_i, L, R) for (int (_i) = L; (i) <= (R); ++(_i))
inline bool isdigit(char ch){return ((ch<='9')and(ch>='0'));}
inline void read(int &x){
    char ch;
    bool flag=false;
    for (ch=getchar();!isdigit(ch);ch=getchar()) if (ch=='-') flag=true;
    for (x=0;isdigit(ch);x=x*10+ch-'0',ch=getchar());
    x=flag?-x:x;
}

struct paper{
    int len;
    int a[MS];

    void scan()
    {
        for(int i = 1; i <= len; i++)
        {
            scanf("%d", &a[i]);
        }
    }

    void print()
    {
        for(int i = 1; i <= len; i++)
        {
            printf("%d ", a[i]);
        }
        puts("");
    }

    bool operator < (const paper& cp)const
    {
        for(int i = 1; i <= len; i++)
        {
            if(a[i] != cp.a[i])
            {
                return (a[i] < cp.a[i]);
            }
        }
        return false;
    }
};

struct matrix{
    int len;
    int c[MS][MS];

    void init(int _len)
    {
        len = _len;
        memset(c, -1, sizeof(c));
    }

    void initRow(int row)
    {
        for(int i = 0; i <= len; i++)
        {
            c[row][i] = -1;
        }
    }

    void initCol(int col)
    {
        for(int i = 0; i <= len; i++)
        {
            c[i][col] = -1;
        }
    }

    void setRow(int row, paper d)
    {
        for(int i = 1; i <= len; i++)
        {
            c[row][i] = d.a[i];
        }
    }

    bool isMatchRow(int row, paper d)
    {
        int cur;
        for(int i = 1; i <= len; i++)
        {
            cur = c[row][i];
            if(-1 != cur && (cur != d.a[i]))
            {
                return false;
            }
        }
        return true;
    }

    void setCol(int col, paper d)
    {
        for(int i = 1; i <= len; i++)
        {
            c[i][col] = d.a[i];
        }
    }

    bool isMatchCol(int col, paper d)
    {
        int cur;
        for(int i = 1; i <= len; i++)
        {
            cur = c[i][col];
            if(-1 != cur && (cur != d.a[i]))
            {
                return false;
            }
        }
        return true;
    }
};

int n;
int cnt[NS];
int ans[NS], tot;
//paper pin[MS * 2 + 1];

int main()
{
   // ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int nCase;
    int ans;
    while(~scanf("%d", &nCase))
    {
        for(int nT = 1; nT <= nCase; nT++)
        {
            memset(cnt, 0, sizeof(cnt));
            scanf("%d", &n);

            int x;
            int num = n + n - 1;
            for(int i = 0; i < num; i++)
            {
                for(int j = 1; j <= n; j++)
                {
                    scanf("%d", &x);
                    cnt[x]++;
                }
            }
            printf("Case #%d:", nT);
            for(int i = 1; i <= 2500; i++)
            {
                if(1 == (cnt[i] & 1))
                {
                    printf(" %d", i);
                }
            }
            puts("");
        }
    }
    return 0;
}


//   __typeof(val.begin()) it = val.begin();
// ios::sync_with_stdio(false);
// cout<<setprecision(30);
