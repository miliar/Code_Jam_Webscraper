#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (int)n; ++i)
#define repf(i, f, l) for(int i = f; i < (int)l; ++i)
#define repit(it, t) for(__typeof((t).begin()) it = (t).begin(); it != (t).end(); it++)

#define endl "\n"

#ifdef ONLINE_JUDGE
#define DEBUG false
#else
#define DEBUG true
#endif

#define pb emplace_back
#define lb lower_bound
#define ul unsigned long
#define ull unsigned long long
#define ll long long
#define INF 1000000007
#define MOD 1000000007
#define fs first
#define sd second
#define DBG0(x) if(DEBUG){ cout << #x << ": " << x << "\t"; }
#define DBG(x) if(DEBUG){DBG0(x); cout << endl;}
#define DBG2(x, y) if(DEBUG){DBG0(x); DBG(y);}
#define DBG3(x, y, z) if(DEBUG){DBG0(x); DBG2(y, z);}
#define DBG4(w, x, y, z) if(DEBUG){DBG0(w); DBG3(x, y, z);}

typedef vector<int> vint;
typedef vector<ll> vll;
typedef vector<ul> vul;
typedef vector<ull> vull;
typedef vector<bool> vbl;
typedef pair<int, int> pii;

inline string case_num(int t){
    ostringstream ret;
    ret << "Case #" << t << ": ";
    return ret.str();
}

class MaxFlow{
    private:
        int n; // num of node
        vector<vint> edge;
    public:
        MaxFlow(int n0){
            n = n0;
            vector<vint> c0(n0, vint(n0));
            edge = c0;
        }
        void addEdge(int x, int y, int w){
            edge[x][y] = w;
        }

        int maxFlow(int s, int t){
            int ret = 0;
            vector<vint> capacity; // set of edge of remainder network
            capacity = edge;
            for(bool cont = true; cont; ){
                cont = false;
                vint par(n, - 1);
                par[s] = s;
                queue<int> que;
                que.push(s);
                while(!que.empty()){
                    int cur = que.front();
                    que.pop();
                    if(cur == t) break;
                    rep(i, n){
                        if(capacity[cur][i] > 0 && par[i] == -1){
                            par[i] = cur;
                            que.push(i);
                        }
                    }
                }
                if(par[t] != -1){
                    cont++;
                    vint path;
                    int cur = t;
                    while(par[cur] != cur){
                        path.pb(cur);
                        cur = par[cur];
                    }
                    path.pb(s);
                    reverse(path.begin(), path.end());
                    int fl = 1000000009;
                    rep(i, path.size() - 1) fl = min(fl, capacity[path[i]][path[i + 1]]);
                    /**** DEBUG ****
                    cout << fl << ": ";
                    rep(i, path.size()) cout << path[i] <<" ";
                    cout << endl;
                     ***************/
                    rep(i, path.size() - 1){
                        capacity[path[i]][path[i + 1]] -= fl;
                        capacity[path[i + 1]][path[i]] += fl;
                    }
                    ret += fl;
                }
            }
            return ret;
        }
};
string solve(vector<double> naomi, vector<double> ken){
    ostringstream oss;
    int n = naomi.size();
    vector<int> ans(2);
    vector<int> a(n);
    vector<int> b(n);
    rep(i, n) a[i] = (naomi[i] * 100000);
    rep(i, n) b[i] = (ken[i] * 100000);
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    rep(k, 2){
        MaxFlow mxf(2 * n + 2);
        rep(i, n){
            rep(j, n){
                if(a[i] > b[j]) 
                    mxf.addEdge(i, n + j, 1);
            }
        }
        rep(i, n){
            mxf.addEdge(2*n, i, 1);
            mxf.addEdge(n + i, 2 * n + 1, 1);
        }
        if(k == 0)
            ans[k] = mxf.maxFlow(2*n, 2*n + 1);
        else
            ans[k] = n - mxf.maxFlow(2*n, 2*n + 1);
        swap(a, b);
    }

    oss << ans[0] << " " << ans[1] << endl;
    return oss.str();
}

int main(void){
    ios::sync_with_stdio(false);
    vector<string> ans;
    vector<future<string>> prcs;
    int t;
    cin >> t;
    rep(num, t){
        int n;
        cin >> n;
        vector<double> naomi(n), ken(n);
        rep(i, n) cin >> naomi[i];
        rep(i, n) cin >> ken[i];
#ifdef ONLINE_JUDGE
        prcs.pb(async(solve, naomi, ken));
#else
        cout << case_num(num + 1) << solve(naomi, ken);
        cerr << case_num(num + 1) << solve(naomi, ken);
#endif

    }
#ifdef ONLINE_JUDGE
    rep(i, t)
        cout << case_num(i + 1) << prcs[i].get();
#endif
    return 0;
}

