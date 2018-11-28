#include <algorithm>
#include <iostream>
#include <cstring>
#include <climits>
#include <limits>
#include <complex>
#include <cassert>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#include <set>

#define type(x) __typeof((x).begin())
#define foreach(it,x) for(__typeof(x.begin()) it = x.begin() ; it!=x.end() ; it++ )

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a,b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

const int inf = 1e9 + 143;
const long long longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

int a[5][5];
int b[5][5];

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    int tc = read();
    for(int it = 1; it <= tc; it++){
        printf("Case #%d: ",it);
        int r1 = read();
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                a[i][j] = read();
            }
        }
        int r2 = read();
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                b[i][j] = read();
            }
        }
        int same = 0, x = -1;
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                if(a[r1][i] == b[r2][j]){
                    x = a[r1][i];
                    same++;
                }
            }
        }
        if(same == 0){
            printf("Volunteer cheated!\n");
        }else if(same == 1){
            printf("%d\n",x);
        }else{
            printf("Bad magician!\n");
        }
    }

    return 0;
}
