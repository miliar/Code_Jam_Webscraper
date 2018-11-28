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
std::ifstream __fin("B-large.in.txt");
std::ofstream __fout("put.out");
#define cin __fin
#define cout __fout
//#endif

vector<bool> pa;
bool was[1024][1024];

void print() {
    for (bool a: pa)
        cout << (a ? '+' : '-');
    cout << endl;
}

inline void flip(int k) {
    reverse(pa.begin(), pa.begin()+k);
    FOR (i, k) pa[i] = !pa[i];
}

ull solve(int k) {
    if (k==0) return 0;
    if (pa[k-1]==true) return solve(k-1);
    if (pa[0]==false) {
        flip(k);
        return 1+solve(k-1);
    }
    int st_f=0; while (pa[st_f]) st_f++;
    flip(st_f+1);
    flip(k);
    return 2+solve(k-1);
}

int test_main() {
    string s; cin >> s;
    pa.clear(); for (char c: s) pa.push_back(c=='+');
    EX(solve(SZ(s)));
}

int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t; RAN (i,1,t) {
        cout << "Case #" << i << ": ";
        test_main();
    }
    return 0;
}












































