#include <iostream>
using namespace std;

int main()
{
    int t, x=0,z;
    int ans1,ans2;
    int a[4][4];
    int b[4][4];
    cin >> t;
    while(t--){
        x++;
        int cnt = 0;
        int flag = 0;
        cin >> ans1;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
            cin >> a[i][j];
            }
        }
        cin >> ans2;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
            cin >> b[i][j];
            }
        }
        if(ans1 == ans2){
            for(int i=0; i<4; i++){
                if(a[ans1-1][i] != b[ans2-1][i]){
                    flag = 1;
                }
            }
            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){
                    if(a[ans1-1][i] == b[ans2-1][j]){
                        cnt++;
                        z = a[ans1-1][i];
                        flag = 2;
                    }
                }
            }
        }
        if(ans1 != ans2){
            for(int i=0; i<4; i++){
                if(a[ans1-1][i] != b[ans2-1][i]){
                    flag = 1;
                }
            }
        }
        if(ans1 != ans2){
            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){
                    if(a[ans1-1][i] == b[ans2-1][j]){
                        z = a[ans1-1][i];
                        cnt++;
                        flag = 2;
                    }
                }
            }
        }
        if(cnt > 1){
            cout << "Case #" << x << ": " << "Bad magician!" << endl;
        }
        else if(flag == 1){
            cout << "Case #" << x << ": " << "Volunteer cheated!" << endl;
        }
        else if(flag == 2){
            cout << "Case #" << x << ": " << z << endl;
        }
    }
    return 0;
}
