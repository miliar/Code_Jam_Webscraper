#include <bits/stdc++.h>

using namespace std;


bool check(string x) {
    int len = (int) x.length();
    int cnt1 = 0, cnt2 = 0;
    for (int i = 1; i < len - 1; i++) {
        if (x[i] == '1') {
            if (i % 2 == 0) {
                cnt1++;
            } else cnt2++;
        }
    }
    return cnt1 == cnt2;
}

string nextString(string x) {
    char buf[40];
    int len = (int) x.length();
    for (int i = 0; i < len; i++) {
        buf[i] = x[i];
    }
    buf[len] = '\0';
    int des = 2;
    while (buf[len - des] == '1') {
        buf[len - des] = '0';
        des++;
    }
    buf[len - des] = '1';
    return string(buf);
}

int main() {
    int t, tcase = 0, n, j;
    cin >> t;
    while (t--) {
        printf("Case #%d:\n", ++tcase);
        cin >> n >> j;
        char tmp[40];
        tmp[0] = '1';
        tmp[n - 1] = '1';
        for (int i = 1; i < n - 1; i++) tmp[i] = '0';
        tmp[n] = '\0';
        string stmp(tmp);
        int cnt = 0;
        while (cnt < j) {
            if (check(stmp)) {
                cout << stmp << " 3 2 5 2 7 2 3 2 11" << endl;
                cnt++;
            }
            stmp = nextString(stmp);
        }
    }
    return 0;
}
