/*
Name: Mahir Asef Kabir
AUST CSE 28th Batch
Problem Name: Problem B. Revenge of the Pancakes
*/
#include <bits/stdc++.h>
using namespace std;

#define FORab(i,a,b) for( __typeof(a)         i = (a);          i <= (b);        ++i )
#define FORba(i,a,b) for( __typeof(a)         i = (a);          i >= (b);        --i )
#define forstl(i, s) for( __typeof((s).end()) i = (s).begin (); i != (s).end (); i++ )
#define rep(i,n)     FORab(i,0,n-1)
#define II           ({int    a;scanf("%d",   &a);a;})
#define IL           ({int64  a;scanf("%lld", &a);a;})
#define ID           ({double a;scanf("%lf",  &a);a;}
#define all(a)       (a).begin(), (a).end()
#define MP           make_pair
#define pb           push_back
#define INF          1<<30
#define int64        long long
#define nl           puts("")
#define vi           vector<int>
#define pii          pair<int,int>
#define PI           3.141592653589793
#define EPS          2.718281828459045
#define memo(a,b)    memset(a,b,sizeof(a))

template < class T, class U > inline T max (T &a, U &b) { return a > b ? a : b; }
template < class T, class U > inline T min (T &a, U &b) { return a < b ? a : b; }
template < class T, class U > inline T swap (T &a, U &b){ T tmp = a;a = b;b = tmp;}
template < class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template < class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template < class X, class Y, class Z > X BigMod( X B, Y P, Z M ) {
    if( P == 0 ) return 1;
    if( P % 2 == 1 ) {
        return ((B%M)*BigMod(B,P-1,M))%M;
    }
    X P2 = BigMod(B,P/2,M);
    return (P2*P2)%M;
}

int main() {
    #ifdef Mahir
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int t = II;
    rep(cs,t) {
        string str;
        cin >> str;
        int n = str.length();
        vector < int > v;
        int sign = 1, cnt = 0;
        rep(i,n) ( str[i] == '+' )?v.pb(1): v.pb(-1);
        FORba( i, n-1, 0 ) {
            if( v[i]*sign < 0 ) {
                sign *= -1;
                cnt++;
            }
        }
        cout << "Case #" << cs+1 << ": " << cnt << endl;
    }
    return 0;
}
