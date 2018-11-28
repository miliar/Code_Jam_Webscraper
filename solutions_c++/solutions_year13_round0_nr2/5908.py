#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int c;
    cin>>c;
    for(int a = 1; a <= c; ++a) {
        int n,m;
        cin>>n>>m;
        vector<int> R(n,0);
        vector<int> C(m,0);
        vector<vector<int> > F(n, vector<int>(m));
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                cin>>F[i][j];
                R[i] = max(R[i],F[i][j]);
                C[j] = max(C[j],F[i][j]);
            }
        }
        bool ok = true;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(F[i][j] < R[i] && F[i][j] < C[j]) ok = false;
            }
        }

        cout<<"Case #"<<a<<": "<<(ok ? "YES" : "NO")<<endl;
    }
    return 0;
}
