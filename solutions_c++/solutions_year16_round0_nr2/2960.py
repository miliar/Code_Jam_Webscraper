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
    string s;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cnt;
    TEST(t){
        cin >> s;
        vector<int> vs;
        forn(i, sz(s))vs.push_back(s[i]=='+'?1:0);
        cnt = 0;
        int i = sz(vs) - 1;

        while(i >= 0){
            while(vs[i] == 1){
                i--;
                if(i < 0)break;
            }
            if(i < 0)break;
            cnt ++;

            int y = -1;
            while(vs[y + 1] == 1)y++;
            forn(j, y + 1)vs[j] = 0;

            if(y >= 0)cnt++;

            reverse(vs.begin(), vs.begin() + i + 1);
            forn(j, i + 1)vs[j] = (vs[j]==1?0:1);
        }
        printf("Case #%d: %d\n", t, cnt);
    }
}
