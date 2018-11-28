#include <iostream>
#include <fstream>

using namespace std;

int T, N, M;
int grid[102][102];
int Max = 0;
bool ans;
void initgrid() {
     for (int i = 0; i <= 101; i++) {
         for (int j = 0; j <= 101; j++) {
             grid[i][j]=-1;
         }
     }
}

bool checknode(int n, int m) {
     int value = grid[n][m];
     if (value == Max) return 1;
     // vertical dir //
     bool ver = 1;
     for (int i = 1; i<=N; i++) {
         if (grid[i][m] > value) ver = 0;
     }
     // horizontal dir //
     bool hor = 1;
     for (int i = 1; i<=M; i++) {
         if (grid[n][i] > value) hor = 0;
     }
     if((!ver)&&(!hor)) return 0;
     else return 1; 
}

int main() {
    ifstream input ("B.in");
    ofstream output ("B.out");
    ofstream debug ("debug.out");
    input >> T;
    
    for (int i = 1; i <= T; i++) {
        ans = 1;
        initgrid();
        Max = 0;
        input >> N >> M;
        for (int n = 1; n<=N; n++) {
            for (int m = 1; m<=M; m++) {
                int ex;
                input >> ex;
                grid[n][m]=ex;
                if (ex > Max) Max = ex;
            }    
        }
        for (int n = 1; n<=N && ans; n++) {
            for (int m = 1; m<=M && ans; m++) {
                //cout << grid[n][m] << " " << checknode(n, m) << "   ";
                if (!checknode(n, m)) ans = 0;
            }
            //cout << endl;
        }
        output << "Case #" << i << ": " << ((ans)?("YES"):("NO")) << endl;
        for (int n = 1; n<=N; n++) {
            for (int m = 1; m<=M; m++) {
                debug << grid[n][m] << " " << checknode(n, m) << "   ";
            }
            debug << endl;
        }
        debug << ((ans)?("YES"):("NO")) << endl << endl;
        
        
    }
    //cin >> T;
    return 0;
}
