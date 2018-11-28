#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("/Users/linsina/Downloads/D-small-attempt0.in", "r", stdin);
    freopen("/Users/linsina/Downloads/D-small-attempt0.out", "w", stdout);
    vector<string> s(2);
    s[0] = "RICHARD";
    s[1] = "GABRIEL";
    int n;
    cin >> n;
    for (int k = 0; k < n; k++) {
        int x, r, c;
        string result;
        cin >> x >> r >> c;
        if (x == 1) result = s[1];
        if (x == 2) {
            if ((r * c) % 2 == 0)
                result = s[1];
            else result = s[0];
        }
        if (x == 3) {
            if (r < 3 && c < 3) result = s[0];
            else if (r < 2 || c < 2) result = s[0];
            else if ((r * c) % 3 != 0) result = s[0];
            else result = s[1];
        }
        if (x == 4) {
            if (r < 4 && c < 4) result = s[0];
            else if (r < 2 || c < 2) result = s[0];
            else if (r * c == 8) result = s[0];
            else result = s[1];
        }
        cout << "Case #" << k + 1 << ": " << result << endl;
    }
    
    return 0;
}


