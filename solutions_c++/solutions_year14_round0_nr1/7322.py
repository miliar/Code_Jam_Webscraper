#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int testNum, row1, row2;
char flag[20];

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int temp, mutual, testCase = 0, result;
    cin >> testNum;

    while (testCase < testNum){
        testCase++;
        memset(flag, 0, 20);
        mutual = 0;

        cin >> row1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++){
                cin >> temp;
                if (i + 1 == row1){
                    flag[temp] = 1;
                }
            }

        cin >> row2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++){
                cin >> temp;
                if (i + 1 == row2 && flag[temp] > 0){
                    mutual++;
                    result = temp;
                }
            }

        switch (mutual){
            case 0:
                cout << "Case #" << testCase << ": Volunteer cheated!" << endl;
                break;
            case 1:
                cout << "Case #" << testCase << ": " << result << endl;
                break;
            default:
                cout << "Case #" << testCase << ": Bad magician!" << endl;
                break;
        }
    }
    return 0;
}
