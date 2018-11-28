
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <map>
#include <cmath>
#include <assert.h>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

#define ABS(X) ( ((X)>0) ? (X) : -(X) )
#define pb push_back

typedef long long int LL;

using namespace std;

template <typename T>
ostream& operator<<(ostream &a, const vector<T> &v) {
    a << "(";
    if (v.size()>=1) a << v[0];
    for (int i=1; i<v.size(); i++) {
        a << ", " << v[i];
    }
    a << ")";
    return a;
}

template <typename T>
ostream& operator<<(ostream &a, const list<T> &v) {
    a << "(";
    for (auto it=v.cbegin(); it != v.cend(); ++it) {
        if (it != v.cbegin()) a << ", ";
        a << *it;
    }
    a << ")";
    return a;
}

int A,B,K;
LL dp[32][8];

int getBit(int mask, int ix) {
    return (mask >> ix) & 1;
}

LL numComb(int ix, int mask) {
    if (ix==-1) return 1;
    if (dp[ix][mask] != -1) return dp[ix][mask];
    int topA = (getBit(mask,0)==1) ? getBit(A,ix) : 1;
    int topB = (getBit(mask,1)==1) ? getBit(B,ix) : 1;
    int topK = (getBit(mask,2)==1) ? getBit(K,ix) : 1;
    
    LL ans = 0;
    repf(a,0,topA) repf(b,0,topB) {
        int k = a&b;
        int nmask = (1-topA+a) | ((1-topB+b)<<1) | ((1-topK+k)<<2);
        if (k <= topK) ans += numComb(ix-1,mask & nmask);
    }
    return dp[ix][mask]=ans;
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    repf(tc,1,T) {
        cin >> A >> B >> K;
        --A;--B;--K;
        rep(i,32) rep(j,8) dp[i][j]=-1;
        cout << "Case #" << tc << ": ";
        cout << numComb(30,7) << endl;
    }
}

