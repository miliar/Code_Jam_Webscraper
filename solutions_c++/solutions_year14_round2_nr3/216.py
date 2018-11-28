
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <map>
#include <cmath>
#include <stack>
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

int N,M;
vector<string> cities;
char adjmat[55][55];

bool possibleOrder(const vector<int> &order) {
    stack<int> st;
    st.push(order[0]);
    for (int i=1; i<order.size(); i++) {
        while (!st.empty() && !(adjmat[st.top()][order[i]])) st.pop();
        if (st.empty()) return false;
        st.push(order[i]);
    }
    return true;
}

string solve() {
    vector<int> perm;
    rep(i,N) perm.pb(i);
    string ans = "z";
    do {
        if (possibleOrder(perm)) {
            string tmp;
            rep(i,N) tmp += cities[perm[i]];
            ans = min(ans,tmp);
        }
    } while (next_permutation(perm.begin(),perm.end()));
    return ans;
}

int main(int argc, char **argv) {
    int T,u,v;
    cin >> T;
    repf(tc,1,T) {
        cin >> N >> M;
        rep(i,N) rep(j,N) adjmat[i][j]=0;
        cities.resize(N);
        rep(i,N) cin >> cities[i];
        rep(i,M) {
            cin >> u >> v;
            --u; --v;
            adjmat[u][v] = 1;
            adjmat[v][u] = 1;
        }
        string ans = solve();
        cout << "Case #" << tc << ": " << ans << endl;
        cities.clear();
    }
}

