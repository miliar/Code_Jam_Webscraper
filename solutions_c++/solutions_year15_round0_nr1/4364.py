#include <iostream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o = 0; o < t; o++) {
        string s;
        int k = 0;
        cin >> k;
        cin >> s;
        k = 0;
        int curr = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (i > curr) {
                k += i - curr;
                curr = i;
            }
            curr += s[i] - '0';
        }
        cout << "Case #" << o + 1 << ": " << k << endl;
    }


    return 0;
}
