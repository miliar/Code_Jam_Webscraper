#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    int r1, r2;
    int a1[5][5], a2[5][5];
    int _case = 0;
    cin >> T;
    while(T--){
        cin >> r1;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++){
                cin >>a1[i][j];
            }
        cin >> r2;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++){
                cin >>a2[i][j];
            }
        int cnt = 0, ans = -1;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++){
                if(a1[r1][i] == a2[r2][j]){
                    cnt++;
                    ans = a1[r1][i];
                }
        }
        cout <<"Case #" << ++_case << ": ";
        if(cnt == 1){
            cout << ans << endl;
        }else if(cnt > 1){
            cout << "Bad magician!" << endl;
        }else cout << "Volunteer cheated!"<< endl;
    }
    return 0;
}
