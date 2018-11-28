#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 25;

int n, k;
int t[N];
vector<int> in[N];
vector<int> st;

int z[(1 << 20) + 1];

int solve(int mask){
    if(mask == (1 << n) - 1)
        return 0;
    if(z[mask] == -1){
        int cnt[210];
        memset(cnt, 0, sizeof(cnt));
        forn(i, sz(st))
            cnt[st[i]]++;
            
        forn(i, n)
            if(mask & (1 << i)){
                cnt[t[i]]--;
                forn(j, sz(in[i]))
                    cnt[in[i][j]]++;
            }
            
        z[mask] = -2;
            
        forn(i, n)
            if((mask & (1 << i)) == 0 && cnt[t[i]] > 0 && solve(mask | (1 << i)) != -2){
                z[mask] = i;
                return i;
            }
        
    }
    
    return z[mask];
}

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests){
        cin >> k >> n;
        st.clear();

        forn(i, k){
            int x;
            scanf("%d", &x);
            st.pb(x);
        }

        forn(i, n){
            in[i].clear();
            int cnt;
            scanf("%d %d", &t[i], &cnt);

            forn(j, cnt){
                int x;
                scanf("%d", &x);
                in[i].pb(x);
            }             
        } 
                
        memset(z, -1, sizeof(z));
        int ans = solve(0);
        
        if(ans == -2)
            printf("Case #%d: IMPOSSIBLE\n", test + 1);
        else{
            printf("Case #%d:", test + 1);
            
            int cur = 0;
            int cnt = 0;
            while(cur != (1 << n) - 1){
                printf(" %d", solve(cur) + 1);
                cur |= (1 << z[cur]);
                cnt++;
            } 
            
            if(cnt != n)
                throw;
            puts("");
        }
    }
    
    return 0;
}
