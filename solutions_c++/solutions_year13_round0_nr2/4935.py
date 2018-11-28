#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, N, M;
    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>N>>M;
        vector< vector< int > > v(N, vector<int>(M));
        for(int n=0; n<N; n++) {
            for(int m=0; m<M; m++) {
                cin>>v[n][m];
            }
        }
        vector<int> minn(N, 0);
        vector<int> minm(M, 0);
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                minn[i] = max(minn[i], v[i][j]);
                minm[j] = max(minm[j], v[i][j]);
            }
        }
        bool good = true;
        for(int i=0; i<N;i ++) {
            for(int j=0; j<M; j++) {
                if(v[i][j] != min(minn[i], minm[j])) good = false;
            }
        }
        cout<<"Case #"<<t<<": ";
        if(good) cout<<"YES\n";
        else cout<<"NO\n";
    }
    return 0;
}