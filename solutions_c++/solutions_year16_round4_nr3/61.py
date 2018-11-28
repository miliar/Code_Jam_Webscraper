#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

int mat[1000];
char dir[110][110];
#define LEFT 0
#define UP 1
#define RIGHT 2
#define DOWN 3
int V[110][110][4];
vi adj[110*110*2];

int main() {
    int ts;
    scanf("%d", &ts);
    rep(t,0,ts) {
        printf("Case #%d:\n", t+1);
        int r, c;
        scanf("%d %d", &r, &c);
        rep(i,0,r+c) {
            int a, b;
            scanf("%d %d", &a, &b);
            a--, b--;
            mat[a] = b;
            mat[b] = a;
        }
        bool found = false;
        rep(s,0,1<<(r*c)) {
            rep(i,0,r) {
                rep(j,0,c) {
                    dir[i][j] = (s & (1<<(i*c+j)) ? '/' : '\\');
                }
            }
// rep(i,0,r) {
//     rep(j,0,c) {
//         printf("%c", dir[i][j]);
//     }
//     printf("\n");
// }
// printf("\n");
            rep(i,0,r) {
                rep(j,0,c) {
                    int a = (i*c+j)*2 + 0,
                        b = (i*c+j)*2 + 1;
                    adj[a].clear();
                    adj[b].clear();
                    if (dir[i][j] == '/') {
                        V[i][j][UP] = a;
                        V[i][j][LEFT] = a;
                        V[i][j][DOWN] = b;
                        V[i][j][RIGHT] = b;
                    } else {
                        V[i][j][UP] = b;
                        V[i][j][RIGHT] = b;
                        V[i][j][LEFT] = a;
                        V[i][j][DOWN] = a;
                    }
                }
            }
            rep(i,0,r) {
                rep(j,0,c) {
                    int a = (i*c+j)*2 + 0,
                        b = (i*c+j)*2 + 1;
                    if (dir[i][j] == '/') {
                        if (j > 0) adj[a].push_back(V[i][j-1][RIGHT]);
                        if (i > 0) adj[a].push_back(V[i-1][j][DOWN]);
                        if (j+1 < c) adj[b].push_back(V[i][j+1][LEFT]);
                        if (i+1 < r) adj[b].push_back(V[i+1][j][UP]);
                    } else {
                        if (j-1 >= 0) adj[a].push_back(V[i][j-1][RIGHT]);
                        if (i+1 < r) adj[a].push_back(V[i+1][j][UP]);
                        if (j+1 < c) adj[b].push_back(V[i][j+1][LEFT]);
                        if (i-1 >= 0) adj[b].push_back(V[i-1][j][DOWN]);
                    }
                }
            }
            map<int,int> num_to_V;
            rep(i,0,c) {
                num_to_V[i] = V[0][i][UP];
            }
            rep(i,0,r) {
                num_to_V[c+i] = V[i][c-1][RIGHT];
            }
            rep(i,0,c) {
                num_to_V[r+c+i] = V[r-1][c-i-1][DOWN];
            }
            rep(i,0,r) {
                num_to_V[r+c+c+i] = V[r-i-1][0][LEFT];
            }
// iter(it,num_to_V) {
//     cout << it->first << " " << it->second << endl;
// }
            bool ok = true;
            iter(it,num_to_V) {
                int cur = it->second,
                    last = -1;

// cout << "simul " << it->first << endl;
// cout << it->second << endl;
                while (true) {
                    int nxt = -1;
                    iter(it,adj[cur]) {
                        if (*it == last) {
                            continue;
                        }
                        assert(nxt == -1);
                        nxt = *it;
                    }
                    if (nxt == -1) {
                        break;
                    }
                    last = cur;
                    cur = nxt;
// cout << cur << endl;
                }
// cout << "wanted " << num_to_V[mat[it->first]] << endl;
                if (num_to_V[mat[it->first]] != cur) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                rep(i,0,r) {
                    rep(j,0,c) {
                        printf("%c", dir[i][j]);
                    }
                    printf("\n");
                }
                found = true;
                break;
            }
        }
        if (!found) {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

