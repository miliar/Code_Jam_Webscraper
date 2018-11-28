
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <queue>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

using namespace std;

typedef long long int LL;

#define MSINF 0x7fffffff;

template<class T>
ostream& operator<<(ostream &a, const vector<T> &v) {
    a<< "[";
    if (v.size() >= 1) a<<v[0];
    for (int i=1; i<v.size(); i++) {
        a << ", " << v[i];
    }
    a << "]\n";
    return a;
}

int N;
vector<int> v;
int tmpvec[1005];

#define SIGN(X) ( ((X)<0) ? -1 : 1 )

bool verify(const vector<int> &v) {
    int i;
    for (i=1; i<v.size(); i++) if (v[i-1] > v[i]) break;
    for (; i<v.size(); i++) if (v[i-1] < v[i]) break;
    return i==v.size();
}

int solve() {
    queue< vector<int> > q;
    map< vector<int>,int > s;
    q.push(v);
    s[v] = 0;
    while ( !q.empty() ) {
        vector<int> current = q.front(); q.pop();
        if (verify(current)) return s[current];
        for (int i=1; i<current.size(); i++) {
            vector<int> cpy = current;
            swap(cpy[i],cpy[i-1]);
            if (s.count(cpy) == 0) {
                s[cpy] = s[current]+1;
                q.push(cpy);
            }
        }
    }
    return -1;
}

int main(int argc, char **argv) {
    int TC;
    cin >> TC;
    rep(tc,TC) {
        cin >> N;
        v.resize(N,0);
        rep(i,N) cin >> v[i];
        int ans;
        if (N>1) ans = solve();
        else ans=0;
        cout << "Case #" << tc+1 << ": " << ans << endl;
    }
}

