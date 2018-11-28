// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
inline int bit( int x, int i ) { return (x>>i)&1; }
#define N 20
char inp[N+1];
double dp[1<<N];
bool vis[1<<N];
int n;
int get( int s, int p, int &q ) {
    int c=n;
    q=p;
    while ( q<n && bit(s,q) ) c--,q++;
    if ( q==n ) q=0;
    while ( q<n && bit(s,q) ) c--,q++;
    return c;
}
double go( int s ) {
    if ( s==(1<<n)-1 ) return 0;
    if ( vis[s] ) return dp[s];
    vis[s]=1;
    double ret=0;
    for ( int i=0; i<n; i++ ) {
        int q=-1;
        ret+=get(s,i,q);
        ret+=go(s|(1<<q));
    }
    ret/=n;
    return dp[s]=ret;
}
void solve() {
    n=strlen(gets(inp));
    int s=0;
    for ( int i=0; i<n; i++ ) if ( inp[i]=='X' ) s|=1<<i;
    memset(dp,0,sizeof(dp));
    memset(vis,0,sizeof(vis));
    double ans=go(s);
    printf("%.12f\n",ans);
}
int main()
{
    int num_case;
    scanf("%d ",&num_case);
    for ( int i=1; i<=num_case; i++ ) {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
