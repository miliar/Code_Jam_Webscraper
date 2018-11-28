#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        int n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << test_index + 1 << ": INSOMNIA\n";
            continue;
        }
        bitset<10> digits;
        int m = 0;
        while (digits.count() != 10) {
            m += n;
            int k = m;
            while (k) {
                digits[k % 10] = 1;
                k /= 10;
            }
        }
        cout << "Case #" << test_index + 1 << ": " << m << "\n";
    }
    return 0;
}
