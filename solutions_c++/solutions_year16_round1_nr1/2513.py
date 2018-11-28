#include <iostream>
#include <string>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        string w;
        w = s[0];
        for(int i = 1; i < s.size(); i++) {
            if(s[i] >= w[0]) w = s[i] + w;
            else w += s[i];
        }
        printf("Case #%d: %s\n", t, w.c_str());
    }
    return 0;
}
