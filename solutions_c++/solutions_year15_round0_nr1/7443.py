#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int T, t = 0;
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    cin >> T;
    while(T--) {
        t++;
        int len;
        string str;
        cin >> len >> str;
        int ans = 0;
        int standing = 0;
        for (int i = 0; i <= len; i++) {
            if (i > standing) {
                ans += (i - standing);
                standing = i;
            }
            standing += str[i] - '0';
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}