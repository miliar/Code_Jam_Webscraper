#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <math.h>
#include <iomanip>
#include <bitset>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long LL;
typedef pair<int,int> pii;
#define CLR(x,y) memset(x,y,sizeof(x));
#define PB push_back
#define MP make_pair
#define FOR(i,x,y) for(int i = (x) ; i < (y) ; ++i)
#define ROF(i,x,y) for(int i = (y)-1 ; i >= (x); --i)
#define FORG(i,x,g) for(int i = g.head[(x)] ; ~i ; i = g.next[i])
#define INF 0x3f3f3f3f

inline LL getint()
{
    int c;
    while(c=getchar(),(c<'0'||c>'9')&&(c!='-')&&(c!=EOF));
    if(c==EOF)return -1;
    bool flag=(c=='-');
    if(flag)
        c=getchar();
    LL x=0;
    while(c>='0'&&c<='9')
    {
        x = (x<<3)+x+x+c-'0';
        c=getchar();
    }
    return flag?-x:x;
}
inline void writeln(LL x)
{
    if(x<0)
    {
        putchar('-');
        x=-x;
    }
}
const int N = 60;
int T;
int n;
LL m;
vector<int> toEnd;
bool slide[N];
void init() {
    toEnd.clear();
    CLR(slide,0);
}
void solve(int n, LL m) {
    LL tmp = 1;
    if(m>(tmp<<(n-2)))return;
    slide[1]=1;
    --m;
    toEnd.push_back(1);
    if(m==0)return;
    int base = 2;
    while(m) {
        if(m&1)toEnd.push_back(base);
        m>>=1;
        ++base;
    }
}
void print(int cas) {
    printf("Case #%d: ", cas);
    if(toEnd.size() == 0) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("POSSIBLE\n");
        for(int i = 0 ; i < toEnd.size() ; ++i)
            slide[toEnd[i]] = 1;
        for(int i = 1 ; i < n ; ++i) {
            for(int j = 1 ; j <= n ; ++j) {
                if(j<=i)printf("0");
                else if(j<n)printf("1");
                else printf("%d",slide[i]);
            }
            printf("\n");
        }
        FOR(j,0,n)printf("0");
        printf("\n");
    }
}
int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(int cas = 1 ; cas <= T ; ++cas) {
        init();
        scanf("%d",&n);
        m = getint();
        solve(n,m);
        print(cas);
    }
}
