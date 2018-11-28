// Danger! Too many bugs! HadronWave (c)
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <functional>


using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const long long mod = 1000000007;

ll binpow(ll a,ll n){
    ll res = 1;
    while(n){
        if(n&1) res *= a;
        a *= a;
        res %= mod;
        a %= mod;
        n >>= 1;
    }
    return res;
}

int row[101],col[101];
int field[101][101];

int main() {
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,n,m,a;
    scanf("%d",&T);

    for(int c = 1;c<=T;++c){
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;++i)
            row[i] = -1;    
        for(int j=1;j<=m;++j)
            col[j] = -1;
            
        for(int i=1;i<=n;++i){
            for(int j=1;j<=m;++j){
                scanf("%d",&field[i][j]);
                row[i] = max(row[i],field[i][j]);
                col[j] = max(col[j],field[i][j]);
            }
        }
        bool bad = false;
        for(int i=1;i<=n && !bad;++i){
            for(int j=1;j<=m && !bad;++j){
                if( field[i][j] < row[i] && field[i][j] < col[j]){
                    bad = true;
                }
            }
        }
        printf("Case #%d: ",c);
        if(bad) printf("NO");
        else printf("YES");
        printf("\n");
    }       

    return 0;
}