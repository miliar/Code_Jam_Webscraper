#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream cin("input");
    ofstream cout("output");

    int t;
    cin >> t;

    for (int l = 0; l < t; l++) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        
        int count = 0;
        int ans = 0;

        for (size_t i = 0; i < s.size(); i++) {
            int c = s[i] - '0';

            if (count < i) {
                ans += i - count;
                count = i;
            }
            count += c;
        }

        cout << "Case #" << l + 1 << ": " << ans << endl;
    }
}
