#include<bits/stdc++.h>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<29)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int> 
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define MOD 1000000007
#define ios ios::sync_with_stdio(0);
#define N 10

int R , C , M , m[N][N];
bool ok , vis[N][N];
int dx[8] = { 1 , -1 , 0 , 0 , 1 , -1 , -1 , 1 };
int dy[8] = { 0 , 0 , 1 , -1 , -1 , 1 , -1 , 1 };

int dfs(int x,int y){
    vis[x][y] = 1;
    int ret = 1 , mines = 0;
    for(int i = 0 ; i < 8 ; i++){
        int u = x + dx[i] , v = y + dy[i];
        if( u >= 0 and u < R and v >= 0 and v < C ){
            if( m[u][v] ) mines = 1;
            if( mines ) return ret;
        }
    }
    for(int i = 0 ; i < 8 ; i++){
        int u = x + dx[i] , v = y + dy[i];
        if( u >= 0 and u < R and v >= 0 and v < C and !vis[u][v] )
            ret += dfs( u , v );
    }
    return ret;
}

void f(){
    vector<int> v( R * C - M , 0 );
    for(int i = 0 ; i < M ; i++)
        v.pb( 1 );
    
    bool solve = 0;
    do{
        if( solve ) break;
        me(m,0);
        for(int i = 0 ; i < v.size() ; i++)
            m[i/C][i%C] = v[i];
        
        for(int i = 0 ; i < R and !solve ; i++){
            for(int j = 0 ; j < C ; j++)if( !m[i][j] ){
                me(vis,0);
                int ret = dfs( i , j );
                if( !solve and ret == R * C - M ){
                    
                    for(int k = 0 ; k < R ; k++){
                        for(int r = 0 ; r < C ; r++){
                            if( m[k][r] ) cout << '*';
                            else if( k == i and r == j ) cout << 'c';
                            else cout << '.';
                        }
                        cout << '\n';
                    }
                    
                    solve = 1;
                    break;
                }
            }
        }
        
    }while( next_permutation( all(v) ) );
    if( solve ) ok = 1;
}

int main(){
    int tc;
    cin >> tc;
    for(int tt = 1 ; tt <= tc ; tt++){
        cin >> R >> C >> M;
        ok = 0;
        cout << "Case #" << tt << ":\n";
        f();
        if( !ok ) cout << "Impossible\n";
    }
    return 0;
}
