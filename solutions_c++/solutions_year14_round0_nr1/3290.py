#include <iostream>

using namespace std;

int main(){
    int T;
    int m1[4][4] = {0};
    int m2[4][4] = {0};
    int r1,r2;
    cin >> T;
    for (int t1 = 1; t1 <= T ; t1++){
        cin >> r1;
        for (int i = 0 ; i < 4 ; i++){
            for (int j = 0 ; j < 4 ; j++){
                cin >> m1[i][j];
            }
        }
        cin >> r2;
        for (int i = 0 ; i < 4 ; i++){
            for (int j = 0 ; j < 4 ; j++){
                cin >> m2[i][j];
            }
        }
        
        bool card[17] = {false};
        
        for (int i = 0 ; i < 4 ; i++){
            card[m1[r1 - 1][i]] = true;
        }
        
        int ans = 0;
        bool flag = false;
        int i;
        for (i = 0 ; i < 4 ; i++){
            int tmp = m2[r2 - 1][i];
            if (card[tmp] == true){
                if (flag == true){
                    cout << "Case #" << t1 << ": Bad magician!" << endl;
                    break;
                }
                flag = true;
                ans = tmp;
            }
        }
    
        if (i == 4 && flag){
            cout << "Case #" << t1 << ": " << ans << endl;
            continue;
        }
        if (!flag){
            cout << "Case #" << t1 << ": Volunteer cheated!" << endl;
            continue;
        }
    }
    return 0;
}