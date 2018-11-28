#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Claim: as long n > 0, i.e. kn that contains a number x
// for all numbers x from 0 to 9 inclusive.

string solve(int n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    vector<bool> nums(10, false);
    int count = 0;

    int cur = n;
    while (count < 10) {
        int x = cur;
        while (x && count < 10) {
            int right = x % 10;
            if (!nums[right]) {
                nums[right] = true;
                ++count;
            }
            x = x / 10;
        }
        if (count == 10) {
            return to_string(cur);
        }
        cur += n;
    }

    return "INSOMNIA"; 
}

int main() {
    int T, n;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << endl;
    }
    return 0;
}
