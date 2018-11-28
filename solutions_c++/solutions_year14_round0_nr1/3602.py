#include <iostream>
using namespace std;
int m1[5][5],m2[5][5];
int p[18];
int main (){
    int T,N,r1,r2,ans;
    cin >> T;
    for(int ca=1;ca<=T;ca++){
        cout << "Case #" << ca << ": ";
        cin >> r1 ;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> m1[i][j];
                p[m1[i][j]] = i+1;
            }
        }
        ans = -1;
        cin >> r2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> m2[i][j];
                if(i+1 == r2 && p[m2[i][j]] == r1){
                    if(ans == -1)ans = m2[i][j];
                    else ans = 17;
                }
            }
        }
        if(ans == 17){
            cout << "Bad magician!\n";
        }else if(ans == -1){
            cout << "Volunteer cheated!\n";
        }else cout << ans << "\n";
    }
    return 0;
}
/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
*/
