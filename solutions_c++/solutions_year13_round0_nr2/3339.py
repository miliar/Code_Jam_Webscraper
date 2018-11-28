#include<iostream>
#include<vector>

using namespace std;

int main () {
    int T; cin >> T;
    for (int step=0; step<T; step++) {    
        cout << "Case #" << step+1 << ": ";
        int N, M; cin >> N >> M;
        vector< vector<int> > lawn(N, vector<int>(M));
        vector<int> vertical(M), horizontal(N);
        for (int i=0; i<N; i++) {
            int max = 0;
            for (int j=0; j<M; j++) {
                cin >> lawn[i][j];
                if (lawn[i][j] > max) 
                    max = lawn[i][j];     
            }    
            horizontal[i] = max;
        }
        for (int j=0; j<M; j++) {
            int max = 0;
            for (int i=0; i<N; i++) {
                if (max < lawn[i][j])
                    max = lawn[i][j];
            }
            vertical[j] = max; 
        }
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++) 
                if (lawn[i][j] < horizontal[i] &&
                    lawn[i][j] < vertical[j]) {
                    cout << "NO" << endl;
                    goto done;               
                } 
        cout << "YES" << endl;
done:   ;                               
    }
}
