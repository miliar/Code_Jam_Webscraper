/// In the name of God

#include <bits/stdc++.h>

#define int long long
char O = char(92);
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define X first
#define Y second
#define all(o) o.begin(), o.end()
const int maxn = 1e5 + 10;
int mot[maxn], a[maxn], col[maxn];
bool mark[maxn];
vector<int>adj[maxn];
int N, M;
inline int gg(int i,int j){return i * M + j;}
inline int gt(int x,int dir){return 4 * x + dir;}
vector<int>comp;
void dfs(int v){
    if(mark[v]) return;
    mark[v] = 1;
    comp.push_back(v);
    for(int u : adj[v])
        dfs(u);
}
int rel[maxn];
void doo(){
    int n, m;
    cin >> n >> m;
    N = n, M = m;
    int num = 2 * (n + m);
    for(int i=0; i<num; i++){
        cin >> a[i];
        a[i]--;
    }
    for(int i=0; i<num; i+=2){
        mot[a[i]] = a[i + 1];
        mot[a[i + 1]] = a[i];
    }
    for(int i=0; i<m; i++)
        rel[i] = gt(gg(0, i), 0);
    for(int i=m; i<m+n; i++)
        rel[i] = gt(gg(i-m,m-1), 1);
    for(int i=m+n; i<m+n+m; i++)
        rel[i] = gt(gg(n-1, m - 1 - (i-m-n) ) , 2);
    for(int i=m+n+m; i<m+n+m+n; i++){
        int x = i - m - n - m;
        rel[i] = gt(gg(n - 1 - x, 0), 3);
    }
    for(int mask = 0; mask < (1<<(n * m) ); mask++){
        for(int i=0; i< n * m * 4; i++)
            adj[i].clear(), mark[i] = 0;
        int cnt = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(mask & (1<<cnt)){
                    adj[gt(cnt, 0)].push_back(gt(cnt, 1));
                    adj[gt(cnt, 1)].push_back(gt(cnt, 0));
                    adj[gt(cnt, 2)].push_back(gt(cnt, 3));
                    adj[gt(cnt, 3)].push_back(gt(cnt, 2));
                }
                else{
                    adj[gt(cnt, 0)].push_back(gt(cnt, 3));
                    adj[gt(cnt, 3)].push_back(gt(cnt, 0));
                    adj[gt(cnt, 2)].push_back(gt(cnt, 1));
                    adj[gt(cnt, 1)].push_back(gt(cnt, 2));
                }
                cnt++;
            }
        }
        for(int i=0; i<n-1; i++){
            for(int j=0; j<m; j++){
                int u = gt(gg(i, j), 2);
                int v = gt(gg(i+1, j), 0);
                //cout << u << "::" << v << endl;
                adj[u].push_back(v);
                adj[v].push_back(u);
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m-1; j++){
                int u = gt(gg(i, j), 1);
                int v = gt(gg(i, j+1), 3);
                //cout << u << "::" << v << endl;
                adj[u].push_back(v);
                adj[v].push_back(u);
            }
        }
        int tot = n * m * 4;
        for(int i=0; i<tot; i++){
            if(!mark[i]){
                dfs(i);
                for(int ver : comp)
                    col[ver] = i;
                comp.clear();
            }
        }
        bool can = 1;
        for(int i=0; i<num; i++){
            for(int j=0; j<num; j++){
                if(i == j) continue;
                if(i == mot[j] && col[rel[i]] != col[rel[j]]){
                    can = 0;
                }
                else if(i != mot[j] && col[rel[i]] == col[rel[j]]){
                    //if(mask == 4) cout << ":X" << i << endl;
                    can = 0;
                }
            }
        }
        if(!can) continue;
        cnt = 0;
        for(int i=0; i<n; i++){
            string res;
            for(int j=0; j<m; j++){
                if(mask & (1<<cnt)) res += O;
                else res += '/';
                cnt++;
            }
            cout << res << endl;
        }
        return;
    }
    cout << "IMPOSSIBLE" << endl;

}
main(){
    freopen("CSi.in", "r", stdin);
    freopen("CSo.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": " << endl;
        doo();

    }

}
