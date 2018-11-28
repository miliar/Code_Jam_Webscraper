#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{
    //freopen("/Users/sancruise7/Developer/CodeJam/input.txt","r",stdin);
    int N;
    int a,b;
    int temp;
    int j,k;
    int row1[4];
    int row2[4];
    cin >> N;
    //cout << N << endl;
    for (k = 0; k < N; k++) {
        
        cin >> a;
        for (j = 0; j < 4 * (a-1) ; j++) {
            cin >> temp;
        }
        for (j = 0; j < 4; j++) {
            cin >> row1[j];
        }
        for (j = 0; j < 4 * (4-a);j++){
            cin >> temp;
        }
        
        cin >> b;
        for (j = 0; j < 4 * (b-1); j++) {
            cin >> temp;
        }
        for (j = 0; j < 4; j++) {
            cin >> row2[j];
        }
        for (j = 0; j < 4 * (4-b);j++){
            cin >> temp;
        }
        /*        this part for test
        for (i = 0; i < 4; i++) {
            cout << row1[i] << " ";
        }
        cout << endl;
        for (i = 0; i < 4; i++) {
            cout << row2[i] << " ";
        }
        cout << endl;
         */
        int count = 0,number = -1;
        for (int m = 0; m < 4; m++) {
            for (int n = 0; n < 4; n++) {
                if (row1[m] == row2[n]) {
                    count ++;
                    number = row1[m];
                }
            }
        }
        if (count == 1) {
            cout << "Case #" << k+1 << ": " <<number << endl;
        }
        if(count > 1){
            cout << "Case #" << k+1 << ": Bad magician!" << endl;
        }
        if (count == 0) {
            cout << "Case #" << k+1 << ": Volunteer cheated!" << endl;
        }
    }
    return 0;
}
