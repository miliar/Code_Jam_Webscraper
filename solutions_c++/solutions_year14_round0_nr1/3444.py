#include <iostream>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int mat[10][10];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    ios::sync_with_stdio(false);
    int T; cin>>T;
    int cas = 0;
    while(T--) {
        int n;
        cin>>n;
        for(int i=1; i<=4; i++) {
            for(int j=1; j<=4; j++) {
                cin>>mat[i][j];
            }
        }
        set<int> s;
        for(int i=1; i<=4; i++) s.insert(mat[n][i]);
        int m;
        cin>>m;
        for(int i=1; i<=4; i++) {
            for(int j=1; j<=4; j++) {
                cin>>mat[i][j];
            }
        }
        int cnt(0), ans(0);
        for(int i=1; i<=4; i++) if(s.find(mat[m][i]) != s.end()) {
            ++ cnt;
            ans = mat[m][i];
        }
        cout<<"Case #"<<++cas<<": ";
        if(cnt == 1) {
            cout<<ans<<endl;
        } else if(cnt > 1) {
            cout<<"Bad magician!"<<endl;
        } else {
            cout<<"Volunteer cheated!"<<endl;
        }
    }

    return 0;
}
