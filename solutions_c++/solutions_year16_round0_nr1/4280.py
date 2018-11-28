#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    for(int a = 1; a <= t; a++) {
        cin >> n;
        int curr = 0;
        if(n == 0)
            cout << "Case #" << a << ": INSOMNIA" << endl;
        else {
            vector<bool> checked(10, false);
            while (!all_of(checked.begin(), checked.end(), [](bool b) { return b; })) {
                curr += n;
                int curr2 = curr;
                while (curr2 != 0) {
                    checked[curr2 % 10] = true;
                    curr2 /= 10;
                }
            }
            cout << "Case #" << a << ": " << curr << endl;
        }
    }
    return 0;
}