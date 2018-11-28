//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
using namespace std;
double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p) memset(p,0,sizeof(p))
#define memf(p) memset(p,0x3f,sizeof(p))
#define memn(p) memset(p,-1,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
typedef long double LD;
const double PI = acos(-1.0);
const LL INF=0x3f3f3f3f3f3f3f3f;
const LL MOD =1000000007ll;
const int maxn =5100000;
int h[100];
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    //map<long long int,int>ma;                 %I64d
    //vector<int>::iterator iter;
    //memset(m,0,sizeof(int));               for(iter=trtr[rt].begin();iter!=trtr[rt].end();iter++)
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d%d",&a,&b);
    //scanf("%d",&n);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    mem(h);
    for(int gg=1;gg<=T;gg++)
    {
        int n,j,t;
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",gg);
        for(LL x=1;x<=j;x++)
        {
            mem(h);
            h[0]=h[n-1]=1;
            t=0;
            LL k=x*2+1,tem,ans;
            for(LL y=0;y<64;y++)
                if(k&(1ll<<y))
                    t=y;
            for(LL y=0;y<=t;y++)
                if(k&(1ll<<y))
                    h[y]=h[n-t+y-1]=1;
            for(LL y=n-1;y>=0;y--)
                printf("%d",h[y]);
            for(LL y=2;y<=10;y++)
            {
                tem=1;
                ans=0;
                for(LL z=0;z<=t;z++)
                {
                    if(k&(1ll<<z))
                        ans+=tem;
                    tem*=y;
                }
                printf(" %I64d",ans);
            }
            printf("\n");
        }
    }
    return 0;
}
