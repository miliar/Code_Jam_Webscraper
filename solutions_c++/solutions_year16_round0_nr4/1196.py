#include <iostream>
#include <cstdint>
using namespace std;

int main(void) {
    int t, k, c, s;
    uint64_t start = 0;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> k >> c >> s;
        cout << "Case #" << i << ":";
        for (int j = 1; j <= s; ++j)
            cout << " " << j;
        cout << endl;
    }
    return 0;
}
