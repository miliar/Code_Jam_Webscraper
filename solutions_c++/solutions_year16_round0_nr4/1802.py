//
//  main.cpp
//  codex
//
//  Created by MarekCerny.com.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;
#define X first
#define Y second
#define EX(x) do{cout<<(x)<<endl;return 0;}while(0)
#define SW(a,b) do{auto ___t=a;a=b;b=___t;}while(0)
//#define endl "\n"
#define SZ(v) (int(v.size()))
#define ALL(v) v.begin(),v.end()
#define IN(arr,x) (unsigned)(&x-&arr[0])
#define AT(arr,x) (unsigned)(x-&arr[0])

#define FOR(i,n) for(int i=0;i<int(n);++i)
#define ROF(i,n) for(int i=int(n)-1;i>=0;--i)
#define RAN(i,b,e) for(int i=b;i<=int(e);++i)
#define NAR(i,b,e) for (int i=e;i>=int(b);--i)

#define ASSERT(i,c) do{if(!(c))exit(i);}while(0)
//#include <cassert>
//#define ASSERT(i,c) assert(c)

typedef __uint128_t lll;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double,double> pdd;

//#ifdef DEBUG
std::ifstream __fin("D-small-attempt1.in.txt");
std::ofstream __fout("put.out");
#define cin __fin
#define cout __fout
//#endif

ll fexp(ll x, ll n) {
    if (n == 0) return 1;
    if (n == 1) return x;
    if (n % 2 == 1) return x*fexp(x, n-1);
    ll tmp = fexp(x, n/2);
    return tmp*tmp;
}

int test_main() {
    //cout << endl;
    ll k, c, s; cin >> k >> c >> s;
    ASSERT(55, s<=k);
    ASSERT(66, c>0);
    ll min_s = max(1LL, k-(c-1));
    //if (k==1) EX(1);
    if (min_s > s) EX("IMPOSSIBLE");
    
    ll b = 0; ll p = 1;
    
    c--;
    FOR (i, c) {
        //cout << (c-i) << "k^" << i << endl;
        //cout << (c-i)*p<< endl;
        b += (c-i)*p;
        p *= k;
    }
    p *= k;
    //cout << p << endl;
    
    FOR (i,s) cout << (b+i)%p+1 << " ";
    //cout << "\nCase ##: ";
    //FOR (i,min_s) cout << (b+i+1) << " ";
    cout << endl;
    
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t; RAN (i,1,t) {
        cout << "Case #" << i << ": ";
        test_main();
    }
    return 0;
}












































