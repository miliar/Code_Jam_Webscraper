#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int num1[5][5], num2[5][5];
bool mark[17];
int N, row1, row2;

int main()
{
  //  freopen("A-small-attempt2.in", "r", stdin);
 //   freopen("A-small-attempt0.out", "w", stdout);
    int Cas, t = 1;
    cin >> Cas;
    while (Cas--) {
        memset(mark, false, sizeof(mark));
        cin >> row1;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                cin >> num1[i][j];
                if (i == row1) mark[num1[i][j]] = true;
            }
        }
        int cnt = 0, ans = 0;
        cin >> row2;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                cin >> num2[i][j];
                if (i == row2) {
                    if (mark[num2[i][j]]) cnt++, ans = num2[i][j];
                }
            }
        }
        cout << "Case #" << t++ << ": ";
        if (cnt == 1) {
            cout << ans << endl;
        } else if (cnt >= 2) {
            cout << "Bad magician!" << endl;
        } else
            cout << "Volunteer cheated!" << endl;
    }
    return 0;
}
