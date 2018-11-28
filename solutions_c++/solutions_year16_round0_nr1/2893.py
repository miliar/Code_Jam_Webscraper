#include <bits/stdc++.h>

#define si(n) scanf("%d", &n)
#define sii(n, m) scanf("%d %d", &n, &m)
#define sc(c) scanf("%c", &c)
#define ss(s) scanf("%s", s)

#define forn(i, n) for(int i = 0 ; i < n ; ++i)
#define forr(i, a, b) for(int i = a ; i < b ; ++i)

#define rforn(i, n) for(int i = n-1 ; i >= 0 ; --i)
#define rforr(i, a, b) for(int i = b-1 ; i >= a ; --i)

#define mset(x, y) memset(x, y, sizeof(x))
#define all(x) x.begin(), x.end()

#define TEST(t) int T; cin >> T; for(int t = 1 ; t <= T ; ++t)

using namespace std;
typedef int ll;

bitset<10> b;

int main(){
    ll n, cnt, ans, r;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    TEST(t){
        si(n);
        b.reset();
        cnt = 0;

        printf("Case #%d: ", t);
        if(n){
            for(int i = 1 ;  ; ++i){
                ans = n*i;
                while(ans > 0){
                    r = ans%10;
                    ans /= 10;
                    if(b[r] == 0){
                        b[r] = 1;
                        cnt++;
                    }
                }
                if(cnt == 10){
                    printf("%d\n", n*i);
                    break;
                }
            }
        }
        else puts("INSOMNIA");
    }

    return 0;
}
