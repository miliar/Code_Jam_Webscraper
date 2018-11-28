#include <bits/stdc++.h>

using namespace std;

int grid1[4][4];
int grid2[4][4];

const string bad = "Bad magician!";
const string cheat = "Volunteer cheated!";

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    cin >> t;
    for(int tt = 1 ; tt <= t ; tt++){
        int ans = 0, r1, r2;
        cin >> r1;
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                cin >> grid1[i][j];
            }
        }
        cin >> r2;
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                cin >> grid2[i][j];
            }
        }
        int c = 0, aux;
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                if(grid1[r1-1][i] == grid2[r2-1][j]){
                    c++;
                    aux = grid1[r1-1][i];
                }
            }
        }
        cout << "Case #" << tt << ": " ;
        if(c == 0){
            cout << cheat;
        } else if ( c == 1){
            cout << aux;
        } else {
            cout << bad;
        }
        cout << endl;
    }
    return 0;
}
