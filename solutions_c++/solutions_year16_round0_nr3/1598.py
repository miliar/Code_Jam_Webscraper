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
std::ifstream __fin("put.in");
std::ofstream __fout("put.out");
#define cin __fin
#define cout __fout
//#endif



inline string to_string(lll n, int base) {
    string s;
    do {
        s.push_back( n%base + '0' );
        n /= base;
    } while(n > 0);
    reverse(ALL(s));
    return s;
}

inline lll to_base(string s, int base) {
    lll r = 0, w = 1;
    ROF (i, SZ(s)) {
        r += ( s[i]-'0' )*w;
        w *= base;
    }
    return r;
}

inline lll get_div(lll n) {
    int pr[25] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
    FOR (i, 25) if (n%pr[i]==0) return pr[i];
    return 1;
}

lll fast_exp(lll x, lll n, lll mod) {
    if (n == 0) return 1;
    if (n == 1) return x%mod;
    if (n % 2 == 1) return x*fast_exp(x, n-1, mod)%mod;
    lll tmp = fast_exp(x, n/2, mod);
    return tmp*tmp%mod;
}
/* is like prime :) */
inline bool is_prime(lll n) {
    srand ((unsigned)time(NULL));
    
    FOR (i, 30) {
        lll ra = lll(rand())<<31 | lll(rand());
        if (fast_exp(ra, n-1, n)!=1) return false;
    }
    return true;
}

int test_main() {
    cout << endl;
    int n, j; cin >> n >> j;
    //cout << n << " " << j << endl;
    int succ = 0;
    lll a[11];
    for (lll k=0; k<(lll(1)<<(n-2)); k++) {
        //lll l = (lll(1)<<(n-1))-k-1;
        string bin = to_string((k<<1) | (lll(1)<<(n-1)) | 1, 2);
        bool jamc = true;
        RAN (b,2,10) {
            a[b] = get_div(to_base(bin, b));
            if (a[b]==1) {
                jamc = false;
                break;
            }
        }
        if (jamc) {
            cout << bin << "\t";
            RAN(b,2,10) cout << to_string(a[b],10) << "\t";
            cout << "\n";
            succ ++;
            if (succ >= (lll)j) break;
        } //else cout << bin << "\n";
        
        if (k % 10 ==0) cout.flush();
    }
    return 0;
    
    //int n; cin >> n;
/*
    cout << endl;
    RAN (i,2,10) {
        int n_base = stoi(bin, nullptr, i);
        cout << i << "\t" << get_div(n_base) << "\t" << n_base << endl;
        
    }
    return 0;*/
}

int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t; RAN (i,1,t) {
        cout << "Case #" << i << ": ";
        test_main();
    }
    return 0;
}












































