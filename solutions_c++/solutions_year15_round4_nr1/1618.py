#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <queue>
#include <stack>
#include <cstring>
#include <set>

using namespace std;
typedef long long ll;
typedef pair<int, int> pi;

const int N = 102 * 102;

vector<string> v;
vector<int> adj[N];
int R, C;

bool _isValid(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

pi dirs[128];
bool hasIn[N];
vector<int> myPoints;


int par[N];
int sz[N];
bool cycle[N];
int getPar(int n){
    return par[n] == n ? n : par[n] = getPar(par[n]);
}

bool areSame(int a, int b){
    return getPar(a) == getPar(b);
}

void join(int a, int b){
    if(areSame(a, b)){
        cycle[getPar(a)] = true;
        return;
    }
    if(cycle[getPar(a)]){
        cycle[getPar(b)] = true;
    }
    sz[getPar(b)] += sz[getPar(a)];
    par[getPar(a)] = getPar(b);
}

void _clear() {
    memset(hasIn, false, sizeof hasIn);
    for (int i = 0; i < N; i++) {
        adj[i].clear();
    }
    myPoints.clear();
    v.clear();
    for(int i = 0; i < N; i++){
        par[i] = i;
        sz[i] = 1;
        cycle[i] = false;
    }
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    //freopen("out.out", "w", stdout);
#else
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;

    dirs['>'] = pi(0, 1);
    dirs['^'] = pi(-1, 0);
    dirs['v'] = pi(1, 0);
    dirs['<'] = pi(0, -1);

    for (int tt = 1; tt <= T; tt++) {

        _clear();

        cin >> R >> C;
        v.resize(R);
        for (int i = 0; i < R; i++) {
            cin >> v[i];
            //cout << v[i] << endl;
        }

        bool impossible = false;
        int dr[] = {1, 0, -1, 0};
        int dc[] = {0, -1, 0, 1};

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (v[i][j] != '.') {
                    myPoints.push_back(i * C + j);
                    int rd = dirs[v[i][j]].first, cd = dirs[v[i][j]].second;
                    for(int k = 1; ; k++){
                        int nr = rd * k + i;
                        int nc = cd * k + j;
                        if(!_isValid(nr, nc)) break;
                        if(v[nr][nc] != '.'){
                            join(i * C + j, nr * C + nc);
                            break;
                        }
                    }

                    bool okay = false;

                    for(int w = 0; w < 4 && !okay; w++){
                        for(int k = 1; !okay ; k++){
                            int nr = dr[w] * k + i;
                            int nc = dc[w] * k + j;
                            if(!_isValid(nr, nc)) break;
                            if(v[nr][nc] != '.'){
                                okay = true;
                                break;
                            }
                        }
                    }

                    if(!okay) impossible = true;
                }
            }
        }

        cout << "Case #" << tt << ": ";
        int ans = 0;
        for(int i = 0; i < myPoints.size(); i++){
            if(getPar(myPoints[i]) == myPoints[i] && !cycle[myPoints[i]]) ans++;
        }
        if(impossible) cout << "IMPOSSIBLE" << '\n';
        else cout << ans << '\n';

    }

    return 0;
}

