#include <bits/stdc++.h>

#define si(n) scanf("%d", &n)
#define sii(n, m) scanf("%d %d", &n, &m)
#define sc(c) scanf("%c", &c)
#define ss(s) scanf("%s", s)

#define sz(x) (int)x.size()

#define forn(i, n) for(int i = 0 ; i < n ; ++i)
#define forr(i, a, b) for(int i = a ; i < b ; ++i)

#define rforn(i, n) for(int i = n-1 ; i >= 0 ; --i)
#define rforr(i, a, b) for(int i = b-1 ; i >= a ; --i)

#define mset(x, y) memset(x, y, sizeof(x))
#define all(x) x.begin(), x.end()

#define TEST(t) int T; cin >> T; for(int t = 1 ; t <= T ; ++t)

using namespace std;
typedef int ll;



int main(){
    int k, c, s, n;
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    TEST(t){
        sii(k, c);
        si(s);
        printf("Case #%d:", t);
        if(c == 1 || k == 1)n = k;
        else n = k - 1;

        if(s < n)puts(" IMPOSSIBLE");
        else{
            for(int i = k - n + 1 ; i <= k ; ++i)printf(" %d", i);
            puts("");
        }
    }

    return 0;
}
