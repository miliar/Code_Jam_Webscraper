//
//  File.cpp
//  Gift
///Users/liudanxiao/Documents/Gift/Gift.xcodeproj
//  Created by liudan.xiao on 14-4-11.
//
//



#include<iostream>
using namespace std;
int A[4][4];
int main()
{
    int num;
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        int flag[20] = {0};
        int N = 0;
        int ans;
        int row1, row2;
        cin >> row1;
        row1 -= 1;
        for (int k = 0; k < 4; k++) {
            for (int j = 0; j < 4; j++)
            {
                cin >> A[k][j];
                if (k == row1)
                    flag[A[k][j]] = 1;
            }
        }
        cin >> row2;
        row2 -= 1;
        for (int k = 0; k < 4; k++) {
            for (int j = 0; j < 4; j++)
            {
                cin >> A[k][j];
                if (k == row2 && flag[A[k][j]] == 1)
                {
                    N++;
                    ans = A[k][j];
                }
            }
        }
        if (N == 0)
        {
            cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
        if (N == 1)
        {
            cout << "Case #" << i+1 << ": " << ans << endl;
        }
        if (N > 1) {
            cout << "Case #" << i+1 << ": Bad magician!" << endl;
        }
        
    }
    return 0;
}