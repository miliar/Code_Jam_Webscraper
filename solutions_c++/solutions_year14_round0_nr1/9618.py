#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve(int caseNumber) {
    int ans1, ans2;
    int arr1[4][4], arr2[4][4], vals[20] = {0};
    cin >> ans1;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            cin >> arr1[i][j];
    cin >> ans2;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            cin >> arr2[i][j];
    for (int i = 0; i < 4; i++) {
        vals[arr1[ans1 - 1][i]]++;
        vals[arr2[ans2 - 1][i]]++;
    }
    int ans = -1, cnt = 0;
    for (int i = 0; i < 20; i++) {
        //cout << vals[i] << ' ';
        if (vals[i] == 2) {
            cnt++;
            ans = i;
        }
    }
    cout << "Case #" << caseNumber << ": ";
    if (cnt == 1) {
        cout << ans << endl;
    } else if (cnt == 0) {
        cout << "Volunteer cheated!" << endl;
    } else {
        cout << "Bad magician!" << endl;
    }

}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
    return 0;
}
