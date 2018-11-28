#include <iostream>
using namespace std;

int main(){
    int t, res, res1, mag[8][8], mag1[8][8];
    int cn =1, cases;
    cin >> t;
    while(cn<=t){
        cin >> res;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                cin >> mag[i][j];

        cin >> res1;

        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                cin >> mag1[i][j];

        int tmp;
        int s=0;
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                if(mag[res][i]==mag1[res1][j]){
                    s++;
                    tmp = mag[res][i];
                }
            }
        }
        if(s==1) cout << "Case #" <<cn << ": " <<tmp << endl;
        if(s>1) cout << "Case #" <<cn << ": Bad magician!" << endl;
        if(s==0) cout << "Case #" <<cn << ": Volunteer cheated!" << endl;
        cn++;
    }
}
