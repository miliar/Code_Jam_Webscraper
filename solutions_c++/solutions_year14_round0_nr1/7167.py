#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int Z;
    cin >> Z;
    for(int test = 1; test <= Z; test++) {
        int row[2];
        int cards[2][17][17];
        vector<int> rows;
        for(int k = 0; k < 2; k++) {
            cin >> row[k];
            for(int i = 1; i <= 4; i++) 
                for(int j = 1; j <= 4; j++)
                    cin >> cards[k][i][j];
            rows.insert(rows.end(),cards[k][row[k]]+1,cards[k][row[k]]+5);
        }
        sort(rows.begin(),rows.end());
        int uni = 0;
        int ret = -1;
        for(int i = 0; i < rows.size(); i++){
            if(rows[i] == rows[i+1]) {
                uni++;
                ret = rows[i];
            }
        }
        cout << "Case #" << test << ": ";
        if(uni == 0)
            cout << "Volunteer cheated!";
        else if(uni == 1)
            cout << ret;
        else cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}

