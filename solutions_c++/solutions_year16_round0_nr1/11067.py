#include <climits>
#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int main() {
    int n;
    cin >> n;
    long in[n];
    for (int i = 0; i < n; ++i) cin >> in[i];

    long max = LONG_MAX;
    for (int i = 0; i < n; ++i) {
        long orig = in[i];
        set<char> used;
        for (long j = 1; j < max; ++j) {
            long prod = j * orig;
            if (prod == 0) break;
            string str = to_string(prod);
            const char *c = str.c_str();
            int len = str.length();
            for (int k = 0; k < len; ++k) used.insert(c[k]);
            if (used.size() == 10) {
                cout << "Case #" << i + 1 << ": " << prod << endl;
                break;
            }
        }
        if (used.size() != 10) cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
    }

    return 0;
}
