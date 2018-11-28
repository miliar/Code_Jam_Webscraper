#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    int numCases;
    cin >> numCases;

    for (int caseNum = 0; caseNum < numCases; caseNum++) {
        int N;
        cin >> N;
        
        int M;
        cin >> M;
        
        vector<vector<int>> lawn;
        
        for (int i = 0; i < N; i++) {
            lawn.push_back(vector<int>(M, 0));
            
            for (int j = 0; j < M; j++) {
                cin >> lawn[i][j];
            }
        }
        
        vector<int> rowMax(N, 0);
        vector<int> colMax(M, 0);
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                rowMax[i] = max(rowMax[i], lawn[i][j]);
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                colMax[j] = max(colMax[j], lawn[i][j]);
            }
        }
        
        vector<vector<int>> newGrid;
        for (int i = 0; i < N; i++) {
            newGrid.push_back(vector<int>(M, 100));
        }
        
        bool equal = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int newVal = 100;
                newVal = min(rowMax[i], newVal);
                newVal = min(colMax[j], newVal);
                
                if (newVal != lawn[i][j]) {
                    equal = false;
                    break;
                }
            }
        }
        
        cout << "Case #" << caseNum + 1 << ": ";
        
        if (equal) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
        
    }
    
    return 0;
}

