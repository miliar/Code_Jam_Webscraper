
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

int N;
vector<string> vs;

int solve() {
    int ans=0;
    vector<int> indices(N,0);
    bool finished=false;
    do {
        bool alleq=true;
        rep(i,N) if(vs[i][indices[i]] != vs[0][indices[0]]) alleq=false;
        if (!alleq) return -1;

        vector<int> lens(N,0);
        rep(i,N) {
            int ix = indices[i];
            char c = vs[i][ix];
            while  ( (ix<vs[i].size()) && (vs[i][ix] == c)) ix++;
            lens[i] = ix-indices[i];
            indices[i] = ix;
            if (ix == vs[i].size()) finished=true;
        }

        sort(lens.begin(), lens.end());
        rep(i,N) {
            ans += ABS(lens[i] - lens[N/2]);
        }
    } while (!finished);
    rep(i,N) if (indices[i] != vs[i].size()) return -1;
    return ans;
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    repf(tc,1,T) {
        cin >> N;
        vs.resize(N);
        rep(i,N) cin >> vs[i];
        int ans = solve();
        cout << "Case #" << tc << ": ";
        if (ans == -1) cout << "Fegla Won\n";
        else cout << ans << endl;
        vs.clear();
    }
}

