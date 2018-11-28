#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<vector<int>> H;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        cin >> N >> M;
        H.resize(N);
        for(int i=0; i<N; ++i) H[i].resize(M);
        for(int i=0; i<N; ++i){
            for(int j=0; j<M; ++j){
                cin >> H[i][j];
            }
        }
        bool can_mow = true;
        for(int i=0; i<N; ++i){
            for(int j=0; j<M; ++j){
                bool c1 = false, c2 = false;
                int r = H[i][j];
                for(int k=0; k<M; ++k){
                    if(H[i][k] > r) c1 = true;
                }
                for(int k=0; k<N; ++k){
                    if(H[k][j] > r) c2 = true;
                }
                if(c1 && c2) can_mow = false;
            }
        }
        if(can_mow) cout << "YES" << '\n';
        else cout << "NO" << '\n';
    }
    return 0;
}
