// Code Jam 2014 A: Magic Trick

#include <iostream>
#include <cstdio>
using namespace std;

int T;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int test = 1; test<=T; test++){
        int ans = 0;
        int row1, row2;
        int match = 0;
        int grid1[4][4], grid2[4][4];
        cin >> row1; row1--;
        for (int i = 0; i<4; i++){
            for(int j=0; j<4; j++){
                cin >> grid1[i][j];
            }
        }
        cin >> row2; row2--;
        for (int i = 0; i<4; i++){
            for(int j=0; j<4; j++){
                cin >> grid2[i][j];
            }
        }

        for (int i = 0; i<4; i++){
            for (int j = 0; j<4; j++){
                if (grid1[row1][i] == grid2[row2][j]){
                    ans = grid1[row1][i];
                    match++;
                }
            }
        }
        if (match==0) cout << "Case #" << test << ": Volunteer cheated!\n";
        if (match==1) cout << "Case #" << test << ": " << ans << "\n";
        if (match>=2) cout << "Case #" << test << ": Bad magician!\n";
    }
}


