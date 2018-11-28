#include <iostream>
#include <vector>

using namespace std;

vector<int> foo() {
    int n;
    cin >> n;
    n--;
    int t;
    vector<int> a;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> t;
            if (i == n) {
                a.push_back(t);
            }
        }
    }
    return a;
}

int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        auto a = foo();
        auto b = foo();
        int count = 0;
        int ans = 0;
        for (auto i : a) {
            for (auto j : b) {
                if (i == j) {
                    if (++count == 1) {
                        ans = i;
                    }
                }
            }
        }
        cout << "Case #" << ca << ": ";
        if (count == 1) {
            cout << ans << "\n";
        } else if (count == 0) {
            cout << "Volunteer cheated!\n";
        } else {
            cout << "Bad magician!\n";
        }
    }
    return 0;
}
