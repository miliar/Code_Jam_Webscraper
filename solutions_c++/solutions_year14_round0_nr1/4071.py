#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    freopen ("in.txt", "r", stdin); freopen ("out.txt", "w", stdout);
    int n, board[4][4], cont[16], row;
    for (int i = 0; i < 16; i++) cont[i]=0;
    cin >> n;

    for (int i = 0; i < n; i++){
        for (int i = 0; i < 16; i++) cont[i]=0;
        cin >> row;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> board[j][k];
        for (int j = 0; j < 4; j++)
            cont[board[row-1][j]-1]++;
        cin >> row;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> board[j][k];
        for (int j = 0; j < 4; j++)
            cont[board[row-1][j]-1]++;
        int max = 0, win; bool rep = 0;
        for (int j = 0; j < 16; j++)
            if (cont[j]>max){max = cont[j]; win = j+1;}
            else if (cont[j]==max && max==2) rep=1;
        if (rep) cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
        else if (max == 1) cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
        else if (max == 2) cout << "Case #" << i+1 << ": " << win << endl;
    }

    return 0;
}
