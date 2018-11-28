#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int grid[100][100];
int max_i[100];
int max_j[100];
int T,N,M;

bool check() {
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
        {
            if(grid[i][j] == max_i[i] 
                || grid[i][j] == max_j[j]) continue;
            else return false;
            
        }
    return true;
}

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    fin >> T;
    for(int tt = 1; tt <= T; tt++) {
        memset(max_i,0,sizeof(max_i));
        memset(max_j,0,sizeof(max_j));
        fin >> N >> M;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++) {
                fin >> grid[i][j];
                if(grid[i][j] > max_i[i]) {
                    max_i[i] = grid[i][j];
                }
                if(grid[i][j] > max_j[j]) {
                    max_j[j] = grid[i][j];
                }
            }
        fout << "Case #" << tt << ": ";
        if(check()) fout << "YES" << endl;
        else fout << "NO" << endl;
    }
    
    
    return 0;
}
