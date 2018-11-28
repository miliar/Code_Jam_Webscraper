#include <algorithm>
#include <iostream>
#include <cstring>
#include <complex>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <bitset>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

#define all(x) (x).begin(), (x).end()
#define type(x) __typeof((x).begin())
#define foreach(it, x) for(type(x) it = (x).begin(); it != (x).end(); it++)

#ifdef KAZAR
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

typedef long long ll;
typedef pair<int, int> ii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 10101;

char chs[5] = "1ijk";

char c1[4][5] = {
"1ijk",
"i1kj",
"jk1i",
"kji1"
};


int cf[4][4] = {
{1,1,1,1},
{1,-1,1,-1},
{1,-1,-1,1},
{1,1,-1,-1}
};

char mul[256][256];
int coef[256][256];

char suff[N];
int csuff[N];
char s[N];

void solve(){
    int n = read();
    int x = read();
    scanf(" %s", s + 1);
    for(int i = n + 1; i <= n * x; i++){
        s[i] = s[i - n];
    }
    n *= x;
    suff[n + 1] = '1';
    csuff[n + 1] = 1;
    for(int i = n; i > 0; i--){
        suff[i] = mul[s[i]][suff[i + 1]];
        csuff[i] = csuff[i + 1] * coef[s[i]][suff[i + 1]];
    }
    char pref = '1';
    int cpref = 1;
    for(int i = 1; i < n; i++){
        cpref *= coef[pref][s[i]];
        pref = mul[pref][s[i]];
        if(pref != 'i' || cpref != 1)
            continue;
        char mid = '1';
        int cmid = 1;
        for(int j = i + 1; j < n; j++){
            cmid *= coef[mid][s[j]];
            mid = mul[mid][s[j]];
            if(mid == 'j' && cmid == 1){
                if(suff[j + 1] == 'k' && csuff[j + 1] == 1){
                    puts("YES");
                    return;
                }
            }
        }
    }
    puts("NO");
}

int main(){
    
#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            mul[chs[i]][chs[j]] = c1[i][j];
            coef[chs[i]][chs[j]] = cf[i][j];
        }
    }
    
    int tc = read();
    
    for(int i = 1; i <= tc; i++){
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}

