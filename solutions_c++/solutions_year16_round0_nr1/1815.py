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

using namespace std;
#define X first
#define Y second
#define EX(x) do{cout<<(x)<<endl;return 0;}while(0)
#define SW(a,b) do{auto ___t=a;a=b;b=___t;}while(0)
#define endl "\n"
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

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double,double> pdd;

//#ifdef DEBUG
std::ifstream __fin("A-large.in.txt");
std::ofstream __fout("put.out");
#define cin __fin
#define cout __fout
//#endif

int test_main() {
    bool arr[10]; fill(arr, arr+10, false);
    ll n; cin >> n;
    ll i, f = 0;
    if (n == 0) EX("INSOMNIA");
    for (i = 1; f<10; i++) {
        for (char c :to_string(i*n)) {
            if (arr[c-'0']==false) {
                arr[c-'0'] = true;
                f++;
            }
        }
    }
    EX((i-1)*n);
}




int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t; RAN (i,1,t) {
        cout << "Case #" << i << ": ";
        test_main();
    }
    return 0;
}












































