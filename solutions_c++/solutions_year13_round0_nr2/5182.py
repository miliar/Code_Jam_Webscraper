#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T,N,M,cell;
    bool result = true;
    
    cin >>T;
    
    for (int i =1; i <= T; i++) {
        cin >>N >>M;
        vector<int> lawn (N*M);
        vector<int> maxH(N,0);
        vector<int> maxV(M,0);
        result = true;
        
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                cin >>cell;
                lawn[(n*M)+m] = cell;
                if (maxV[m] < lawn[(n*M)+m]) maxV[m] = lawn[(n*M)+m];
                if (maxH[n] < lawn[(n*M)+m]) maxH[n] = lawn[(n*M)+m];
            }
        }

        if (N == 1 || M == 1) result = true;
        for (int n = 0; n < N && result; n++) {
            for (int m = 0; m < M && result; m++) {
                if (lawn[(n*M)+m] < maxV[m] && lawn[(n*M)+m] < maxH[n]) result = false;
            }
        }
        
        cout <<"Case #" <<i <<": ";
        if (result) cout <<"YES";
        else cout <<"NO";
        cout <<endl;
    }
}
