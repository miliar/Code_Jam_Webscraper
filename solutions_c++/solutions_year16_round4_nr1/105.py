#include <bits/stdc++.h>

using namespace std;

const int Inf = 1e9 + 7;

int T, cas, a[5], b[5], n;

string Gao(int win, int cur) {
    if (cur == 0) {
        a[win] --;
        string st;
        st.push_back(win + '0');
        return st;
    }
    string a = Gao(win, cur - 1);
    string b = Gao((win + 1) % 3, cur - 1);
    if (a < b) return a + b;
    else return b + a;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        printf("Case #%d: ", ++ cas);
        cin >> n;
        cin >> b[1] >> b[0] >> b[2];
        string res = "IMPOSSIBLE";
        for (int i = 0; i < 3; i ++) {
            for (int j = 0; j < 3; j ++)
                a[j] = b[j];
            string t = Gao(i, n);
//            cout << t << endl;
//            system("pause");
            bool flag = 0;
            for (int j = 0; j < 3; j ++)
                if (a[j] != 0) flag = 1;
            if (flag) continue;
            if (res == "IMPOSSIBLE") {
                res = t;
            } else if (res < t) {
                res = t;
            }
        }
//        printf("%s\n", res.c_str());
        if (res == "IMPOSSIBLE") puts("IMPOSSIBLE");
        else {
            for (int i = 0; i < res.size(); i ++) {
                if (res[i] == '0') printf("P");
                if (res[i] == '1') printf("R");
                if (res[i] == '2') printf("S");
            }
            puts("");
        }
    }
}
