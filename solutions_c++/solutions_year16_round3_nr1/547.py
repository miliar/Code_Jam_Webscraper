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
int T;
const int N = 40;
pair<int,int> senator[N];
priority_queue<pair<int,int> > pq;
int n;
int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    FOR(cas,1,T+1) {
        scanf("%d",&n);
        FOR(i,0,n) {
            int x;
            scanf("%d",&x);
            pq.push(MP(x,i));
        }
        printf("Case #%d: ",cas);
        while(pq.size()>2) {
            pair<int,int> tmp = pq.top();
            pq.pop();
            printf("%c ",'A'+tmp.second);
            --tmp.first;
            if(tmp.first)pq.push(tmp);
        }
        senator[1] = pq.top();
        pq.pop();
        senator[0] = pq.top();
        pq.pop();
        senator[1].first = senator[1].first-senator[0].first;
        FOR(k,0,senator[1].first)
            printf("%c ",'A'+senator[1].second);
        FOR(k,0,senator[0].first)
            printf("%c%c ",'A'+senator[0].second,'A'+senator[1].second);
        printf("\n");
    }
}
