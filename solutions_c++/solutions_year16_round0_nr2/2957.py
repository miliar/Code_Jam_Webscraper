#include <iostream>
using namespace std;

int proc(string s) {
    int j = 0, cnt = 0;
    while (j < s.size()) {
        if (s[j] == '-') {
            cnt++; 
            while (j < s.size() && s[j] == '-') j++;
        }
        if (s[j] == '+') {
            cnt++;
            while (j < s.size() && s[j] == '+') j++;
        }
    }

    if (s[0] == '-') {
        if (cnt & 1) return cnt;
        else return cnt - 1;
    } else {
        if (cnt & 1) return cnt - 1;
        else return cnt;
    }
}

int main() {
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> s;
        cout << "Case #" << i << ": " << proc(s) << endl;
    }
    return 0;
}
