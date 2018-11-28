#include <iostream>

using namespace std;
int main () {
    int numOfCases;
    cin >> numOfCases;
    int row1, row2;
    int arr1[4][4];
    int arr2[4][4];
    int caseNum = 0;
    while(numOfCases--) {
    cin >> row1;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4;j++)
            cin >> arr1[i][j];

    cin >> row2;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4;j++)
            cin >> arr2[i][j];
    caseNum ++;
    cout << "Case #" << caseNum << ": ";
  //  cout << row1 << " " << row2 << " ";
    int flag = 0;
    int num = -1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
//            cout << arr1[row1 - 1][i] << " " << arr2[row2 -1][j] << " ";
            if (arr1[row1 - 1][i] == arr2[row2 - 1][j]) {
                num = arr1[row1 - 1][i];
                flag++;
                //cout << num << " " << i << " " << j;
            }
        }
    }

    if (flag == 0) 
        cout << "Volunteer cheated!";
    else if (flag == 1)
        cout << num;
    else
        cout << "Bad magician!";
    cout << endl;
    }
}

