#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, ans1, ans2, ans;
    int arr[4][4], arr2[4][4];
    set<int> A, B;
    vector<int> C;

    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> ans1;
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                cin >> arr[j][k];
            }
        }

        cin >> ans2;
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                cin >> arr2[j][k];
            }
        }

        for (int j = 0; j < 4; ++j) {
            A.insert(arr[ans1 - 1][j]);
            B.insert(arr2[ans2 - 1][j]);
        }

        set_intersection(A.begin(), A.end(), B.begin(), B.end(), back_inserter(C));

        if (C.size() == 0)
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
        else if (C.size() > 1)
            cout << "Case #" << i << ": Bad magician!" << endl;
        else
            cout << "Case #" << i << ": " << *(C.begin()) << endl;

        A.clear();
        B.clear();
        C.clear();
    }
}
