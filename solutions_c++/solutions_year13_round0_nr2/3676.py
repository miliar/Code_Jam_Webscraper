#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;

int main() {
    int t;
    cin>>t;
    for (int k = 0; k < t; k++) {
        int N, M;
        cin>>N>>M;
        bool visited[N][M];
        int rowMaximum[N];
        int columnMaximum[M];
        vector<vector<int> > lawn;
        lawn.resize(N);
        for (int i = 0; i < N; i++) {
            int max = 0;
            for (int j = 0; j < M; j++) {
                int x;
                cin >> x;   
                if (x > max) 
                    max = x;              
                lawn[i].push_back(x);                
            }
            rowMaximum[i] = max;
        }
       
        for (int i = 0; i < M; i++) {
            int max = 0;
            for (int j = 0; j < N; j++) {
                if (lawn[j][i] > max)
                    max = lawn[j][i];
            }
            columnMaximum[i] = max;
        }       
    
        bool isPossible = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(lawn[i][j] >= rowMaximum[i] || lawn[i][j] >= columnMaximum[j])
                    continue;
                else {
                    isPossible = false;
                    break;
                }
            }
            if (!isPossible)
                break;
        }
        if (isPossible)
            cout << "Case #" << k+1 <<": YES" <<endl;
        else
            cout << "Case #" << k+1 <<": NO" <<endl;
    }
  
}


