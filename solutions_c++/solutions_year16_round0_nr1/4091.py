#include <iostream>
#include <set>

using namespace std;

int t;
int n;

int main() {
    cin >> t;
    for (int k = 1; k <= t; k++) {
        cin >> n;
        if (n == 0) {
            cout << "Case #" << k << ": INSOMNIA" << endl;
        } else {
            int i = 1;
            int count = 0;
            set<int> history;
            // n * 1, n * 2, ...
            while (1) {
                // cal i * n
                int target = i * n;
                while (target) {
                    int digit = target % 10;
                    if (history.find(digit) == history.end()) {
                        history.insert(digit);
                        count++;
                    }
                    target /= 10;
                }
                if (count == 10) {
                    cout << "Case #" << k << ": " << i * n << endl;
                    break;
                }
                i++;
            }
        }
        
    }
    return 0;
}