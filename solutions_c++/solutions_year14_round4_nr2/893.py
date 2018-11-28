#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define x first
#define y second
#define PB push_back
#define REP(i,n) for (int i = 0; i < int(n); ++i)
#define FORE(i,a,b) for (int i = int(a); i <= int(b); ++i)
#define debug(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef queue<int> Q;
typedef priority_queue<int> PQ;

template <class Ta, class Tb> inline Tb cast(Ta a) {stringstream ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const ll INF = 1000000000000000000LL;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

int good(vector<int>& v) {
    int n = v.size();
    int mx = 0;
    for (int i=0;i<n;++i) if (v[i] > v[mx]) mx=i;
    for (int i=1;i<=mx;++i) {
        if (v[i-1]>v[i]) return 0;
    }
    for (int i=mx+1;i<n;++i) {
        if (v[i-1]<v[i]) return 0;
    }
    return 1;
}

void escr(vector<int>& v) {
    int n = v.size();
    for (int i=0;i<n;++i) cout << v[i] << " ";
    cout << endl;
}

int main() {
    int t; cin >> t;
    for (int cas=1; cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        int n;
        cin >> n;
        vector<int> v(n);
        REP(i,n) cin >> v[i];
        map<Vi, int> m;
        queue<Vi> q;
        m[v] = 0;
        q.push(v);
        bool fi=0;
        int ans=-1;
        if (good(v)) {
            fi=1;
            ans=0;
        }
        while(!q.empty() and !fi) {
            Vi w = q.front(); q.pop();
            int r = m[w];
            for (int i=1;!fi and i<n;++i) {
                swap(w[i-1], w[i]);
                vector<int> z=w;
                if (!m.count(z)) {
                    if (good(z)) {
                        fi=1;
                        ans=r+1;
                    }
                    m[z] = r + 1;
                    q.push(z);
                }
                swap(w[i-1], w[i]); //leave original
            }
        }
        cout << ans << endl;
    }
}
