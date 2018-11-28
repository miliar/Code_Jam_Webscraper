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

const int N = 20050;

li n, x, y;
ld z[2][N];

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests){
        li start = clock();
    
        printf("Case #%d: ", test + 1);
        cin >> n >> x >> y;
        //cin >> n;
        //x = 1000 + rand() % 1000;
        //y = 1000 + rand() % 1000;
        x = abs(x);
        
        li layer = (x + y); 
        li sum = 0;
        for(int i = 0; i < layer; i += 2){
            sum += 2*i + 1;
        }
        
        if(sum >= n){
            puts("0.0");
            continue;
        }
        n -= sum;
        
        if(x == 0){
            if(n >= 2*layer + 1)
                puts("1.0");
            else
                puts("0.0");
            continue;
        }
        
        if(n >= 2*layer){
            puts("1.0");
            continue;
        }
        
        li need = y + 1;        

        forn(i, N)
            z[0][i] = 0;
        z[0][need] = 1;
        for(int i = 1; i <= n; ++i){
            int cur = (i & 1);
            int prev = 1 - cur;
            
            forn(j, need + 1)
                z[cur][j] = 0;
            
            forn(j, need + 1){
                if(j == 0){
                    z[cur][j] += z[prev][j];
                    continue;
                }
                
                int c2 = need - j;
                int c1 = i - 1 - c2;
                if(c1 == layer)
                    z[cur][j - 1] += z[prev][j];
                else{
                    z[cur][j - 1] += z[prev][j] * ld(0.5);
                    z[cur][j] += z[prev][j] * ld(0.5);
                }
            }
        }
        
        printf("%lf\n", (double)z[n & 1][0]);
        fprintf(stderr, "Case #%d solved in %I64d\n", test + 1, clock() - start);
    }
    
    return 0;
}
