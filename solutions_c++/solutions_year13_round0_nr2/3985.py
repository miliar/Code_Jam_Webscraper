#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        int yes = 1, n, m;
        cin >> n >> m;
        int **grid = new int*[n];
        int *vMax = new int[m], *hMax = new int[n];
        for(int j=0; j<n; j++){
            grid[j] = new int[m];
            for(int k=0; k<m; k++){
                cin >> grid[j][k];
            }
        }
        for(int j=0; j<n; j++){
            hMax[j] = 0;
            for(int k=0; k<m; k++)
                hMax[j] = hMax[j] < grid[j][k] ? grid[j][k] : hMax[j];
        }
        for(int j=0; j<m; j++){
            for(int k=0; k<n; k++)
                vMax[j] = vMax[j] < grid[k][j] ? grid[k][j] : vMax[j];
        }
        for(int j=0; j<n; j++){
            for(int k=0; k<m; k++){
                if(hMax[j]>grid[j][k] && vMax[k]>grid[j][k]){
                    yes = 0;
                    break;
                }
            }
        }
        cout << "Case #" << (i+1) << ": " << (yes ? "YES" : "NO") << "\n";
    }
    return 0;
}
