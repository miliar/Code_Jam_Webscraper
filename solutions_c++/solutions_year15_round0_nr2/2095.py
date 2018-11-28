#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define mk make_pair
#define pb push_back
#define fst first
#define snd second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
int vec[10000],n;
#define N 1111

int dp[N][N];
int mklss( int x, int k ) {
        if( x <= k ) return 0;
        if( x/2 <=k && (x+1)/2 <= k ) return 1;

        if( dp[x][k] != -1 ) return dp[x][k];

        return dp[x][k] = 1+mklss(x-k,k);
}

int tx( int k ) {
        int ret = 0;
        for( int i = 0; i<n; i++ ) {
               ret += mklss(vec[i],k); 
        }
        return ret;
}

int main(){
        int t,ca=1;
        cin >> t;
        memset( dp, -1, sizeof dp );
        while( t-- )
        {
                cin >> n;
                int MM = 0;
                for( int i = 0; i<n; i++ ) {
                        cin >> vec[i];
                        MM = max(MM,vec[i]);
                }

                int ans = INF;
                for( int i = 1; i<=MM; i++ )
                        ans = min(ans, tx(i) + i );

                cout << "Case #" << ca++ << ": ";
                cout << ans << "\n";

        }
        

        return 0;
}
