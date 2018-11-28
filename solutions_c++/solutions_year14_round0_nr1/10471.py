#include<iostream>
using namespace std;
int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int answer;
        int find = 0;
        int r1;
        int row[4];
        cin >> r1;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                int tmp;
                cin >> tmp;
                if (j == r1) row[k] = tmp;
            }
        }
        int r2;
        cin >> r2;
        for (int j = 1; j <=4; j++) {
            for (int k = 0; k < 4; k++) {
                int n;
                cin >> n;
                if (j != r2) continue;
                for (int l = 0; l < 4; l++) {
                    if (row[l] == n) {
                        find++;
                        answer = n;
                    }
                }
            }
        }
        cout << "Case #" << i << ": ";
        if (find == 1) cout << answer;
        else if (find == 0|| r1 < 1 || r1 >4 || r2 < 1 || r2 > 4) 
            cout << "Volunteer cheated!";
        else cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
