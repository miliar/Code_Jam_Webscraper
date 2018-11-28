#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        int n;
        long long sol;
        vector <int> seen(10, 0);
        cin >> n;
        sol = n;
        if (n == 0) {
            cout << "Case #" << tc + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        for (int i = 0; ;sol += n) {
            for (long long temp = sol; temp > 0; temp /= 10) {
                seen[temp%10] = 1;
            }
            int sleep = 1;
            for (int j = 0; j < 10; j++) {
                if (seen[j] == 0) {
                    sleep = 0;
                    break;
                }
            }
            if (sleep == 1)
                break;
        }
        cout << "Case #" << tc + 1 << ": " << sol << endl;
    }
    return 0;
}