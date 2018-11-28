#include <iostream>

using namespace std;

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n; cin >> n;
        int sum = 0; int added = 0;
        for (int i = 0; i <= n; ++i) {
            char c; cin >> c; int curr = c - 48;
            if (sum + added < i) {
                added += i - (sum + added);
            }
            sum += curr;
        }
        cout << "Case #" << t << ": " << added << endl;
    }
    return 0;
}
