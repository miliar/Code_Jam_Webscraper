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
#define SZ(v) int(v.size())

int m,n;
vector<string> v;

struct Node {
    char c;
    map<char,int> e;
};

void add(vector<Node>& T, string& s) {
    int r = s.size();
    int u = 0;
    for (int i=0;i<r;++i) {
        if (!T[u].e.count(s[i])) {
            Node z; z.c=s[i];
            T[u].e[s[i]]=SZ(T);
            u = SZ(T);
            T.push_back(z);
        }
        else u=T[u].e[s[i]];
    }
}

int triecost(vector<string>& w) {
    //create a trie with the strings on w
    vector<Node> T(1);
    Node z; z.c='@';
    T[0] = z;
    for (int i=0;i<SZ(w);++i) add(T,w[i]);
    return SZ(T);
}

int mx;
vector<int> mxrep;

//f[i] = how many on server i
void rec(int p, vector<int>& w, vector<int>& f) {
    if (p==m) {
        for (int i=0;i<n;++i) if (f[i]==0) return; //non-empty
        int ans=0;
        for (int i=0;i<n;++i) { //can be done in O(M) instead m*n.. np
            vector<string> vs;
            for (int j=0;j<m;++j) if (w[j]==i) {
                vs.push_back(v[j]);
            }
            ans+=triecost(vs);
        }
        mxrep[ans]++;
        mx=max(mx,ans);
    }
    else {
        for (int i=0;i<n;++i) {
            w[p] = i;
            f[i]++;
            rec(p+1,w,f);
            f[i]--;
        }
    }
}

int main() {
    /*vector<string> zz(4);
    zz[0]="AAA";
    zz[1]="AAB";
    zz[2]="AB";
    zz[3]="B";
    cout << triecost(zz) << endl;*/ 
    int t; cin >> t;
    for (int cas=1; cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        cin >> m >> n;
        v = vector<string>(m);
        REP(i,m) cin >> v[i];
        mx=0;
        vector<int>w(m,0);
        vector<int>f(n,0);
        mxrep = vector<int>(10000,0);
        
        rec(0,w,f);
        cout << mx << " " << mxrep[mx] << endl;
    }
}
