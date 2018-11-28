#include <iostream>

using namespace std;

int main(){
    int T,a,b,i,j;
    int card1[4][4],card2[4][4],arr_a[4],arr_b[4];
    cin >> T;
    for(int index = 1 ; index <= T ; index++){
        cin >> a;
        for(i = 0 ; i < 4 ; ++i){
            for(j = 0 ; j < 4 ; ++j){
                cin >> card1[i][j];
                if(i == (a-1)){
                    arr_a[j] = card1[i][j];
                }
            }
        }
        cin >> b;
        for(i = 0 ; i < 4 ; ++i){
            for(j = 0 ; j < 4 ; ++j){
                cin >> card2[i][j];
                if(i == (b-1)){
                    arr_b[j] = card2[i][j];
                }
            }
        }
        int num = 0,ans;
        for(i = 0 ; i < 4 ; ++i){
            for(j = 0 ; j < 4 ; ++j){
                //cout << arr_a[i] << " : " << arr_b[j] << endl;
                if(arr_a[i] == arr_b[j]){
                    num++;
                    ans = arr_a[i];
                }
            }
        }
        if(num == 1){
            cout << "Case #" << index << ": " << ans << endl;
        }else if(num > 1){
            cout << "Case #" << index << ": Bad magician!\n";
        }else{
            cout << "Case #" << index << ": Volunteer cheated!\n";
        }
    }
    return 0;
}
