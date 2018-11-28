#include <iostream>
#include <algorithm>

#define N 4

using namespace std;

int main() {
    int t, row;
    int num[N];
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> row;
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                int x;
                cin >> x;
                if (j == row - 1) {
                    num[k] = x;
                }
            }
        }
        cin >> row;
        int count = 0;
        int result = 0;
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                int x;
                cin >> x;
                if (j == row - 1) {
                    count += std::count(&num[0], &num[N], x);
                    if (count > 0 && result == 0) {
                        result = x;
                    }
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (count == 1) {
            cout << result << endl;
        } else if (count > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }
    }
    return 0;
}
