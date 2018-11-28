#include <bits/stdc++.h>
#include <string>

using namespace std;

int T;

bool was[10];

bool registered(int x) {
    static string s_x;
    s_x = std::to_string(x);

    for (int i = 0; i < s_x.size(); i++) {
        was[s_x[i] - '0'] = true;
    }

    bool flag = true;
    for (int i = 0; i < sizeof(was); i++) {
        flag &= was[i];
    }

    return flag;
}

string get_ans(int n) {
    if (n == 0) {
        return "INSOMNIA";
    }

    memset(was, false, sizeof(was));

    int i = 1;
    while (!registered(i * n))
        i++;

    return std::to_string(i * n);
}

inline void print_ans(string s) {
    static int case_num = 0;
    case_num++;
    cout << "Case #" << case_num << ": " << s << "\n";
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    ios_base::sync_with_stdio(false);

    cin >> T;

    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        print_ans(get_ans(n));
    }
}
