#include <iostream>

using namespace std;

int main(){
    int T;
    int a[4][4], b[4][4];
    cin >> T;
    for(int i=0; i<T; i++){
        int r1, r2;
        cin >> r1;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                cin >> a[j][k];
            }
        }
        cin >> r2;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                cin >> b[j][k];
            }
        }
        int found = 0;
        int num;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                if(a[r1-1][j]==b[r2-1][k]){
                    found++;
                    num = a[r1-1][j];
                }
            }
        }
        cout << "Case #" << i+1 << ": ";
        if(found==1){
            cout << num << endl;
        }else if(found>1){
            cout << "Bad magician!" << endl;
        }else{
            cout << "Volunteer cheated!" << endl;
        }
    }
}
