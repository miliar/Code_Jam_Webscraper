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

const int N = 200;

int n, m;
int a[N][N];

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests){
        printf("Case #%d: ", test + 1);
        
        cin >> n >> m;
        
        forn(i, n)
            forn(j, m)
                scanf("%d", &a[i][j]);

        bool good = true;
                
        forn(i, n){
            forn(j, m){
                bool gv = true;
                forn(k, n)
                    if(a[k][j] > a[i][j]){
                        gv = false;
                        break;
                    }
                    
                bool gh = true;
                forn(k, m)
                    if(a[i][k] > a[i][j]){
                        gh = false;
                        break;
                    }
                    
                if(!gv && !gh){
                    good = false;
                    break;
                }
            }
            
            if(!good)
                break;
        }
        
        puts(good ? "YES" : "NO");
                
                
    }
    
    return 0;
}
