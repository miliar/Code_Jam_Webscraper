#include<cstring>
#include <cassert>
#include<stack>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<fstream>
#include<climits>
#include<memory.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<iterator>
#include<map>
#include<sstream>
#include<set>
#include<limits>
#include<queue>

#ifdef h0me
#define FILES freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILES //freopen("cooling.in","r",stdin);freopen("cooling.out","w",stdout);
#endif

#define all(c) (c).begin(), (c).end()

using namespace std;

typedef long long Long;
typedef long double Double;
namespace Helper
{
    template<typename T> inline string inttos(T x){ostringstream q;q << x;return q.str();}
    inline int stoint( string str){istringstream in(str);int res;in >> res;return res;}
    inline Long stolong(string str){istringstream in(str);Long res;in >> res;return res;}
    template<typename T> inline T pow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
    template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}
    inline int rand() { long long q = 1ll*rand()*RAND_MAX+rand(); return q % INT_MAX; }
    inline int abs(int x) { if (x<0) return -x;else return x; }
    const int MAXINT = 0x7FFFFFFF;
}


const Double EPS = 1e-10;

int main() {
    FILES;
    ios_base::sync_with_stdio(false);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        cout << "Case #" << test+1 << ": ";
        int n;

        string s;
        cin >> n;
        cin >> s;
        int sum = 0;
        int res = 0;
        for (int i = 0; i <= n; ++i) {
            if (sum<i) {
                res+=i-sum;
                sum = i;
            }
            sum+=s[i]-'0';
        }
        cout << res << endl;
    }
    return 0;
}
