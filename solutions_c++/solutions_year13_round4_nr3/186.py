#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
using namespace std;


const int N = 2012;

int A[N];
int B[N];
int ans[N], deg[N];

vector<int> adj[N];
int n;

void solve() {
    int n;
    scanf ( "%d", &n );

    for ( int i = 0; i < n; ++i ) {
        scanf ( "%d", &A[i] );
        adj[i].clear();
    }
    for ( int i = 0; i < n; ++i )
        scanf ( "%d", &B[i] );
    memset ( ans, 0, sizeof ( ans ) );
    memset ( deg, 0, sizeof ( deg ) );

    for ( int i = 0; i < n; ++i ) {
        int tag = 1;
        for ( int j = i - 1; j >= 0; --j )
            if ( A[j] >= A[i] ) {
                adj[i].push_back ( j );
            } else if ( A[j] + 1 == A[i] && tag ) {
                adj[j].push_back ( i );
                tag = 0;
            }
    }
    for ( int i = n - 1; i >= 0; --i ) {
        int tag = 1;
        for ( int j = i + 1; j < n; ++j )
            if ( B[i] <= B[j] ) {
                adj[i].push_back ( j );
            } else if ( B[i] == B[j] + 1 && tag ) {
                adj[j].push_back ( i );
                tag = 0;
            }
    }
    for ( int i = 0; i < n; ++i )
        for ( int j = 0;j < adj[i].size();++j ) {
            int v = adj[i][j];
            ++deg[v];
        }
    for ( int k = 0; k < n; ++k ) {
        int cur;
        for ( int i = n - 1; i >= 0; --i )
            if ( deg[i] == 0 ) cur = i;
        deg[cur] = -1;
        ans[cur] = k + 1;
        for ( int i = 0; i < adj[cur].size(); ++i ) {
            int v = adj[cur][i];
            --deg[v];
        }
    }
    for ( int i = 0; i < n; ++i )
        printf ( " %d", ans[i] );
    printf ( "\n" );
}

int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        printf ( "Case #%d:", t );
        solve();
    }
    return 0;
}