#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    unordered_map<string, string> m;
    m["ij"] = "k"; m["ji"] = "-k";
    m["jk"] = "i"; m["kj"] = "-i";
    m["ki"] = "j"; m["ik"] = "-j";

    m["ii"] = m["jj"] = m["kk"] = "-1";
    m["1i"] = "i"; m["1j"] = "j"; m["1k"] = "k";

    for (int testCase = 1; testCase <= T; testCase++) {
        int x, l;
        cin >> l >> x;
        string t, ans, s;
        cin >> t;
        while (x) {
            if (x & 1) s += t;
            t += t;
            x >>= 1;
        }

        string prod = "1", targets[] = { "i", "j", "k" };
        int idx = 0;
        for (int i = 0; i < s.length(); i++) {            
            if (prod[0] == '-') {
                prod = "-" + m[prod.substr(1, 1) + s[i]];
            } else {
                prod = m[prod + s[i]];
            }
            if (prod[0] == '-' && prod[1] == '-') {
                prod = prod.substr(2, 1);
            }

            if (idx < 2 && prod == targets[idx]) {
                idx++;
                prod = "1";
            }
        }
        ans = ((idx == 2 && prod == targets[2]) ? "YES" : "NO");
        cout << "Case #" << testCase << ": " << ans << endl;
    }
    return 0;
}