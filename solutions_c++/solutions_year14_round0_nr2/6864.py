#include<iostream>
#include<cassert>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<iterator>
#include<ctime>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<queue>
#include <memory.h>

using namespace std;

#define all(c) (c).begin(), (c).end()

template<typename T> inline string intToString(T x){ostringstream q;q << x;return q.str();}
template<typename T> inline T myPow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}


typedef unsigned long long LLong;
typedef long double LDb;

const int MOD = 1000000007;

int used[17];


int main()
{
#ifdef m0stik
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
#else
//    freopen("river.in","r",stdin);
    //freopen("river.out","w",stdout);
#endif
    int test;
    cin >> test;
    for (int tt = 0; tt < test; ++tt) {
        double c,f,x;
        cin >> c >> f >> x;
        long double t = 0;
        long double v = 2.0;\
        long double res = x/v;
        int n;
        for (n = 1;; ++n) {
            long double nt = t+c/v;
            long double nv = v+f;
            long double nres = nt+x/nv;
            //cout << nres - res << "#";
            if (nres-1>res)
                break;

            if (nres<res) {
                res = nres;
            }
            t = nt;
            v = nv;
        }
        //cout << endl;
        //cout << n << endl;
        cout << "Case #" << tt+1 << ": ";
        cout.precision(10);
        cout << fixed << (double)res<< endl;
    }
    
    return 0;
} 