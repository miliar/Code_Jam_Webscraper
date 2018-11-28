#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int f(bool used[4], vector<int> v, int x, int t[5][5]) {
    if(x == v.size()) return 1;
    int ok = 0;

    for(int j = 0; j < 5; ++j) {
        if(t[v[x]][j] && !used[j]) {
            ok = 1;
            used[j] = 1;
            if(f(used, v, x+1, t)== 0) return 0;
            used[j] = 0;
        }
    }
    return ok;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin>>tt;
    for(int xx = 0; xx < tt; ++xx) {
        cout<<"Case #"<<xx+1<<": ";
        int n;
        cin>>n;
        int t[5][5];
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                char q;
                cin>>q;
                if(q == '1') t[i][j] = 1;
                else t[i][j] = 0;
            }
        }
        int ans = 1e9;
        for(int i = 0; i < (1<<(n*n)); ++i) {
            int cnt = 0;
            int t2[5][5] = {0};
            vector<int> v(n);
            for(int j = 0; j < n*n; ++j) {
                int x = j%n;
                int y = j/n;
                t2[x][y] = t[x][y];
                if((1<<j) & i) {
                    ++cnt;
                    if(t[x][y] == 1) goto ohi;
                    t2[x][y] = 1;
                }
            }
            for(int i = 0; i < n; ++i) {
                v[i] = i;
            }
            do {
                bool used[4] = {0};
                if(f(used, v, 0, t2) == 0) {
                    goto ohi;
                }
            }while(next_permutation(v.begin(), v.end()));
                ans = min(ans, cnt);

            ohi:;
        }
        cout<<ans<<'\n';
    }
}
