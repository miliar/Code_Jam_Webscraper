#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<functional>
#include<complex>
#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef vector<int> VI;
typedef vector<string> VS;
const double pi=acos(-1.0);
const double eps=1e-11;

template<class T> inline T sqr(const T& x) { return x*x; }
template<class T> inline void checkmin(T &a,const T& b) { if (b<a) a=b; }
template<class T> inline void checkmax(T &a,const T& b) { if (b>a) a=b; }
#define two(X) (1<<(X))
#define contain(S,X) ((S&two(X))>0)
#define twoL(X) (((int64)1)<<X)
#define containL(S,X) ((S&twoL(X))>0)
template<class T> int countbit(T n) { int R=0; for (;n>0;n&=(n-1)) R++; return R; }
template<class T> T lowbit(T n) { return (n^(n-1))&n; }
template<class T> T gcd(T a,T b) { return (b==0)?a:gcd(b,a%b); }
template<class T> T lcm(T a,T b) { return a*(b/gcd(a,b)); }
template<class T> void out(const vector<T> &a) { cout<<"array: "; for (int i=0;i<SIZE(a);i++) cout<<a[i]<<" "; cout<<endl; cout.flush(); }
#define MARK(n) printf("MARK %d  LINE: %d\n",n,__LINE__);

int main() {
    int T, n;
    cin >> T;

    for (int t=0; t<T; ++t) {
        int a, b, k;
        cin >> a >> b >> k;

        long long ans = 0;

        for (int i=0; i<a; ++i) {
            for (int j=0; j<b; ++j) {
                if ((i & j) < k) {
                    ans++;
                    //cout << i << "  " << j << endl;
                }
            }
        }

        cout << "Case #" << t+1 << ": " << ans << endl; 
    }
    return 0;
}
