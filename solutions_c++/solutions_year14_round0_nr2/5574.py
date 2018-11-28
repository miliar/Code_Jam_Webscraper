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

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    int tc = read();
    for(int it = 1; it <= tc; it++){
        printf("Case #%d: ",it);
        double c, f, x;
        scanf(" %lf %lf %lf",&c,&f,&x);
        double l = 0, r = 50000;
        for(int bit = 0; bit < 100; bit++){
            double m = (l + r) / 2.0;
            double t = 0, gain = 2.0, cur = 0.0;
            while(t < m){
                if((m - t) * gain + cur >= x){
                    cur = x;
                    break;
                }
                if(cur < c){
                    double tneed = (c - cur) / gain;
                    double pass;
                    if(t + tneed > m){
                        pass = m - t;
                    }else{
                        pass = tneed;
                    }
                    t += pass;
                    cur += pass * gain;
                }else{
                    double tleft = m - t;
                    if(tleft * gain < tleft * (gain + f) - c){
                        cur -= c;
                        gain += f;
                    }else{
                        cur += tleft * gain;
                        t += tleft;
                    }
                }
            }
            if(cur >= x)
                r = m;
            else
                l = m;
        }
        printf("%.7lf\n",r);
    }

    return 0;
}
