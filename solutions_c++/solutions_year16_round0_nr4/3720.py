#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << tc + 1 << ": ";
        for (int i = 0; i < k; i++){
            cout << i+1 << " ";
        }
        cout << endl;
    }
    return 0;
}