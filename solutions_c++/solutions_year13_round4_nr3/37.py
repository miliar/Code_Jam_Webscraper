// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cassert>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
// #define assert(x) if (!(x)) { puts("QQ"); return; }
using namespace std;
#define N 2010
int x[N],a[N],b[N];
bool e[N][N],vis[N];
int deg[N];
void solve() {
    int n;
    scanf("%d",&n);
    for ( int i=0; i<n; i++ ) scanf("%d",a+i);
    for ( int i=0; i<n; i++ ) scanf("%d",b+i);
    memset(e,0,sizeof(e));
    for ( int i=0; i<n; i++ ) for ( int j=i+1; j<n; j++ ) {
        if ( a[i]>=a[j] ) e[j][i]=1;
        if ( b[i]<=b[j] ) e[i][j]=1;
    }
    for ( int i=0; i+1<n; i++ ) {
        if ( a[i]<a[i+1] ) e[i][i+1]=1;
        else e[i+1][i]=1;
        if ( b[i]<=b[i+1] ) e[i][i+1]=1;
        else e[i+1][i]=1;
    }
    for ( int i=0; i<n; i++ ) {
        for ( int j=i-1; j>=0; j-- ) if ( a[j]==a[i]-1 ) {
            e[j][i]=1;
            break;
        }
        for ( int j=i+1; j<n; j++ ) if ( b[j]==b[i]-1 ) {
            e[j][i]=1;
            break;
        }
    }
    memset(deg,0,sizeof(deg));
    for ( int i=0; i<n; i++ ) for ( int j=0; j<n; j++ ) if ( e[i][j] ) deg[j]++;
    memset(vis,0,sizeof(vis));
    for ( int i=1; i<=n; i++ ) {
        int w=n;
        for ( int j=0; j<n; j++ ) if ( !vis[j] && deg[j]==0 ) {
            w=j;
            break;
        }
        assert(w!=n);
        vis[w]=1;
        x[w]=i;
        for ( int j=0; j<n; j++ ) if ( e[w][j] ) deg[j]--;
    }
    for ( int i=0; i<n; i++ ) printf("%d%c",x[i],i==n-1?'\n':' ');
    for ( int i=0; i<n; i++ ) {
        int aa=1;
        for ( int j=0; j<i; j++ ) if ( x[i]>x[j] ) aa=max(aa,a[j]+1);
        assert(aa==a[i]);
    }
    for ( int i=n-1; i>=0; i-- ) {
        int bb=1;
        for ( int j=n-1; j>i; j-- ) if ( x[i]>x[j] ) bb=max(bb,b[j]+1);
        //if ( bb!=b[i] ) printf("%d: %d, %d\n",i,b[i],bb);
        assert(bb==b[i]);
    }
}
int main()
{
    int num_case;
    scanf("%d",&num_case);
    for ( int i=1; i<=num_case; i++ ) {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}

