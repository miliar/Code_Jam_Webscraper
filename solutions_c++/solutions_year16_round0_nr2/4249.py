#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        string s; cin >> s;
        int ret = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == '-' && s[i - 1] == '+')
                ret += 2;
        }
        if (s[0] == '-')
            ret++;
        cout<< "Case #" << t <<": " <<  ret << endl;
    }
    return 0;
}
