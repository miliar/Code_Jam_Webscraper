#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        int N, M;
        cin >> N >> M;
        
        int patt[N][M];        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> patt[i][j];
            }
        }
        
        int lawn[N][M];        
        int max;
        
        for (int j = 0; j < M; j++) {
            max = 1;
            for (int i = 0; i < N; i++) {
                if (patt[i][j] > max){
                    max = patt[i][j];
                }
            }
            for (int i = 0; i < N; i++) {
                lawn[i][j] = max;
            }            
        }
        
        for (int i = 0; i < N; i++) {
            max = 1;
            for (int j = 0; j < M; j++) {
                if (patt[i][j] > max){
                    max = patt[i][j];
                }
            }
            for (int j = 0; j < M; j++) {                
                if (max < lawn[i][j]) {                    
                    lawn[i][j] = max;
                }
            }            
        }
        
        bool flag = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (lawn[i][j] != patt[i][j]) {
                    flag = false;
                }
            }
        }
        string res = "NO";
        if (flag) {
            res = "YES";
        }
        
        cout << "Case #" << x << ": " << res << endl;
    }
}