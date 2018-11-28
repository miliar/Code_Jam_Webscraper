#include <algorithm>

#include <deque>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    int numTests = 0;
    cin >> numTests;
    for (int test = 1; test <= numTests; ++test) {
        unsigned int a, b, k, ans = 0;
        cin >> a >> b >> k;

        set<unsigned int> s;
        for (unsigned int i = 0; i < k; ++i) {
            s.insert(i);
        }

        for (unsigned int i = 0; i < a; ++i) {
            for (unsigned int j = 0; j < b; ++j) {
                unsigned int x = i & j;
                if (x < k) {
                    ++ans;
                    s.erase(x);
                }
            }
        }

        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}
