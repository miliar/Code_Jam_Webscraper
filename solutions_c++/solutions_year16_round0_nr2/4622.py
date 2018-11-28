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

const int MXN = 110;
const int MXK = 20;

char s [MXN];


int solve(){
    int cur = 1;
    scanf("%s", s);

    int n = strlen(s);
    rep(i,n){
        if(s[i]=='+') s[i] = 1;
        else s[i] = 0;
    }

    int res = 0;
    for( int i = n-1; i>=0; i-- ){
        if(s[i]!=cur){
            res++;
            cur = 1-cur;
        }
    }
    return res;
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    rep(i,T){
        printf("Case #%d: %d\n", i+1, solve());
    }


    return 0;
}
