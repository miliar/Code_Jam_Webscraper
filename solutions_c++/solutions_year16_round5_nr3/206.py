#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef ONLINE_JUDGE
#define dbg(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;
#else
#define dbg(x)
#endif

#define ff first
#define ss second
typedef long double ld;
typedef pair<ld, pair<ld, ld> > vec;
#define X first
#define Y second.first
#define Z second.second
#define sq(x) (x)*(x)
const int MAXN = 1024;
vec pos[MAXN];
vec vlc[MAXN];
ld S;
ld len(vec v1, vec v2){
    return sqrt(sq(v1.X - v2.X) + sq(v1.Y - v2.Y) + sq(v1.Z - v2.Z));
}

ld dist[MAXN][MAXN];
void solve(){
    int n; cin >> n;
    cin >> S;
    for (int i = 0; i < n; i++){
        cin >> pos[i].X >> pos[i].Y >> pos[i].Z;
        cin >> vlc[i].X >> vlc[i].Y >> vlc[i].Z;
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            dist[i][j] = len(pos[i], pos[j]);
        }
    }
    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]));
            }
        }
    }
    cout << fixed << setprecision(10) << dist[0][1] << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
