#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main(){
    int t, tt = 0, vans_1, vans_2, mat1[4][4], mat2[4][4];
    cin >> t;
    while(t--){
        tt++;
        int tot = 0, ans = 0;
        cin >> vans_1;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> mat1[i][j];
        cin >> vans_2;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> mat2[i][j];
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(mat1[vans_1 - 1][i] == mat2[vans_2 - 1][j]){
                    tot ++;
                    ans = mat1[vans_1 - 1][i];
                }
                if(tot > 1){
                    ans = -1;
                    break;
                }
            }
            if(ans == -1){
                break;
            }
        }
        cout << "Case #" << tt << ": ";
        if(ans == -1){
            cout << "Bad magician!" <<  endl;
        }
        if(ans == 0){
            cout << "Volunteer cheated!" << endl;
        }
        if(ans >= 1){
            cout << ans << endl;
        }
    }
    return 0;
}
