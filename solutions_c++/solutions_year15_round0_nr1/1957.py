#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int smax;
        cin >> smax;
        string s;
        cin >> s;
        int count = 0, toadd = 0;
        for (int i = 0; i <= smax; i++) {
            if (s[i] != '0') {
                toadd = max(toadd, i - count);
                count += int(s[i] - '0');
            }
        }
        cout << "Case #" << testCase << ": " << toadd << endl;
    }
    return 0;
}
