#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, i, r1, r2;
    int a[4][4], b[4][4];
    cin >> t;
    for (i = 1; i <= t; i++){
        cin >> r1;
        for (int j = 0; j < 4; j++){
            for (int k = 0;k < 4;k++){
                cin >> a[j][k];
            }
        }
        cin >> r2;
        for (int j = 0; j < 4; j++){
            for (int k = 0;k < 4;k++){
                cin >> b[j][k];
            }
        }
        vector<bool> pr(17, false);
        for (int j = 0; j < 4; j++){
            pr[a[r1-1][j]] = true;
        }
        int cmn = -1, cnt = 0;
        for (int j = 0; j < 4; j++){
            int n = b[r2-1][j];
            if (pr[n]){
                cmn = n;
                cnt++;
            }
        }
        if (cnt == 0) {
            cout << "Case #" << i << ": Volunteer cheated!\n";
        } else if (cnt == 1) {
            cout << "Case #" << i << ": " << cmn << "\n";
        } else {
            cout << "Case #" << i << ": Bad magician!\n";
        }
    }
}
