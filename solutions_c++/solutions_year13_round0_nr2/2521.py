#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int T, N, M, a;
    bool bout = false;
    cin >> T;
    for (int i=0;i<T;i++){
        bout = false;
        cin >> N >> M;
        int L[N][M];
        for (int j=0;j<N;j++){
            for (int k=0;k<M;k++){
                cin >> L[j][k];
            }
        }
        for (int j=0;j<N;j++){
            for (int k=0;k<M;k++){
                int test[M];
                for (int h=0;h<M;h++){
                    test[h] = L[j][h];
                }
                sort(test,test+M);
                if (L[j][k] == test[M-1]){
                   continue;
                }
                int test2[N];
                for (int h=0;h<N;h++){
                    test2[h] = L[h][k];
                }
                sort(test2,test2+N);
                if (L[j][k] == test2[N-1]){
                   continue;
                } else {
                   cout << "Case #" << i+1 << ": NO" << endl;
                   bout = true;
                   break;
                }
            }
            if (bout) break;
        }
        if (bout) continue;
        cout << "Case #" << i+1 << ": YES" << endl;
    }
}
