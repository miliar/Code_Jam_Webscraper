#include <bits/stdc++.h>
#define rep(i,s,t) for (int i=(s); i<=(t); ++i)
using namespace std ;

#define quant pair<pair<int,int>,pair<int,string>>
#define cons(a,b,c,d) {{a,b},{c,d}}
#define firsts first.first
#define seconds first.second
#define third second.first
#define fourth second.second

const int maxn = 18,maxm = 5;
int n,r,p,s ;
quant f[maxn][maxm] ;

template<class T>
inline void get(T &n) {
    char c = getchar();
    while (c!='-' && (c<'0' || c>'9')) c = getchar();
    n = 0; T s = 1; if (c=='-') s = -1,c = getchar();
    while (c>='0' && c<='9') n*=10,n+=c-'0',c=getchar();
    n *= s;
}

int main() {

    int Test ;
    get(Test);
    rep(Ti,1,Test) {
        get(n); get(r); get(p); get(s);
        printf("Case #%d: ",Ti);
        f[0][0] = cons(1,0,0,"P") ;
        f[0][1] = cons(0,1,0,"R") ;
        f[0][2] = cons(0,0,1,"S") ;

        rep(i,1,n) {
            rep(j,0,2) {
                int k = (j+1) % 3 ;
                quant tmp = cons( f[i-1][j].firsts + f[i-1][k].firsts ,
                        f[i-1][j].seconds + f[i-1][k].seconds ,
                        f[i-1][j].third + f[i-1][k].third ,
                        "" ) ;
                string s1 = f[i-1][j].fourth ;
                string s2 = f[i-1][k].fourth ;
                if ( s1 <= s2 ) tmp.fourth = s1+s2 ;
                else            tmp.fourth = s2+s1 ;
                f[i][j] = tmp ;

            }
        }

        string ans = "IMPOSSIBLE" ;
        rep(j,0,2)
            if ( f[n][j].firsts == p && f[n][j].seconds == r && f[n][j].third == s ) {
                if ( ans == "IMPOSSIBLE" || f[n][j].fourth < ans )
                    ans = f[n][j].fourth ;
            }
        cout << ans << "\n" ;
    }
}
