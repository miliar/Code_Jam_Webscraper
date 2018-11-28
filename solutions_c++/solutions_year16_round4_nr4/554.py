#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 20;


int n;

int bst = 0;

int a [MXN][MXN];

int was [MXN];

bool check(){
    vector<int> p1 (n);
    
    rep(i,n) p1[i] = i;
    
    do{
        vector<int> p2 (n);
        rep(i,n) p2[i] = i;
        do{
            rep(i,n){
                bool empty = true;
                forn(j,i,n){
                    if(a[p1[i]][p2[j]]){
                        empty = false;
                        break;
                    }
                }
                if(empty) return false;
                if(!a[p1[i]][p2[i]])
                    break;
            }
        }while(next_permutation(p2.begin(), p2.end()));
    }while(next_permutation(p1.begin(), p1.end()));
    
    return true;
}

void dfs(int i, int j, int cur){
    if(j==n) i++, j = 0;
    if(i==n){
        if(check()){
            bst = min(bst, cur);
        }
        return ;
    }
    
    if(a[i][j]){
        dfs(i, j+1, cur);
        return ;
    }
    a[i][j] = 1;
    dfs(i, j+1, cur+1);
    a[i][j] = 0;
    dfs(i, j+1, cur);
}

char s [MXN];

int solve(){
    scanf("%d", &n);
    rep(i,n){
        scanf("%s", s);
        rep(j,n){
            a[i][j] = s[j] - '0';
        }
    }
    
    bst = n * n;
    dfs(0, 0, 0);
    
    return bst;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
    

    int T;
    scanf("%d", &T);
    //cout << "kek";
    rep(i,T){
        printf("Case #%d: %d\n", i+1, solve());
    }

    return 0;
}
