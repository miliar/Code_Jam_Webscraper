#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        string s;
        int k;
        cin >> s >> k;
        int result = 0;
        for (int i = 0; i+k <= s.size(); i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j) {
                    s[i+j] = (s[i+j] == '-') ? '+' : '-';
                }
                result++;
            }
        }
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                result = -1;
            }
        }
        if (result >= 0) {
            cout << "Case #" << cas << ": " << result << endl;
        } else {
            cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
        }
    }
}
