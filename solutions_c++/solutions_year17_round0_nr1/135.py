#include <iostream>
#include <cstring>
using namespace std;

int flip[2100];
void go() {
    string s;
    cin >> s;
    int d;
    cin >> d;
    memset(flip, 0, sizeof(flip));
    int cur = 0;
    int ans = 0;
    for (int i = 0; i < s.size(); i++) {
        cur += flip[i];
        if (cur % 2 != (s[i] != '+')) {
            if (i+d > s.size()) {
                cout << "IMPOSSIBLE";
                return;
            }
            flip[i + d]++;
            ans++;
            cur++;
        }
    }
    cout << ans;
}
int main() {
    int testn;
    cin >> testn;
    for (int testi = 0; testi < testn; testi++) {
        cout << "Case #" << testi+1 << ": ";
        go();
        cout << '\n';
    }
}
