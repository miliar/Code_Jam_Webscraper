#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include "assert.h"

#define For(i,a,b) for(__int128 i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((__int128)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

int main() {
    int garbage; cin>>garbage;

    int N, J; cin>>N>>J;
    cout << "Case #1:" << endl;

    __int128 P = 100000;
    __int128 S[P];
    rep(i,P) {
        S[i] = true;
    }
    S[0] = false;
    S[1] = false;
    vector<__int128> primes;
    for(__int128 i=2; i<P; i++) {
        if(S[i]) {
            primes.push_back(i);
            for(__int128 k=2*i; k<P; k+=i) {
                S[k] = false;
            }
        }
    }


    map<vector<__int128>, vector<__int128> > res;
    while(res.size() < J) {
        vector<__int128> curvec;
        curvec.push_back(1);
        rep(i, N-2) {
            curvec.push_back(rand() % 2);
        }
        curvec.push_back(1);
    
        vector<__int128> proof;
        __int128 cur;
        __int128 base;
        for(base=2; base<=10; base++) {
            cur = 0;
            __int128 weight=1;
            for(__int128 i=N-1; i>=0; i--) {
                cur += curvec[i] * weight;
                weight *= base;
            }
            bool good = false;
            for(__int128 x : primes) {
                if(x >= cur) {
                    break;
                }
                if((cur/x)*x == cur) {
                    good = true;
                    proof.push_back(x);        
                    break;
                }
            } 
            if(!good) {
                break;
            }
        }
        if(base == 11) {
            cerr << "FOUND" << endl;
            res[curvec] = proof;
        }
    }
    for(auto x : res) {
        for(auto y : x.first) {
            cout << (int)y;
        }
        cout << " ";
        for(auto y : x.second) {
            cout << " " << (int)y;
        }
        cout << endl;
    }
}
