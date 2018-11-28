#include <bits/stdc++.h>

using namespace std;

int n;
string tmp, s;
pair<bool, char> mul[4][4];
bool sub_s_rez_bool[10001][10001];
char sub_s_rez_char[10001][10001];

pair<bool, char> substr_ans(int L, int R) {
    return make_pair(sub_s_rez_bool[L][R], sub_s_rez_char[L][R]);
}

bool get_ans() {
    int L1 = 0;
    for (int L2 = 1; L2 < n - 1; L2++) {
        for (int L3 = L2 + 1; L3 < n; L3++) {
            pair<bool, char> p1 = substr_ans(L1, L2);
            pair<bool, char> p2 = substr_ans(L2, L3);
            pair<bool, char> p3 = substr_ans(L3, n);
            //cerr << "[" << L1 << ", " << L2 << ") -> " << p1.first << " " << p1.second << "\n";
            //cerr << "[" << L2 << ", " << L3 << ") -> " << p2.first << " " << p2.second << "\n";
            //cerr << "[" << L3 << ", " << n << ") -> " << p3.first << " " << p3.second << "\n";
            if (p1.first && p2.first && p3.first &&
                (p1.second == 'i') &&
                (p2.second == 'j') &&
                (p3.second == 'k')) {
                    return true;
            }
        }
    }
    return false;
}

int c2int(char c) {
    if (c == '1') {
        return 0;
    }
    else if (c == 'i') {
        return 1;
    }
    else if (c == 'j') {
        return 2;
    }
    else {
        return 3;
    }
}

int main() {
    ios::sync_with_stdio(0);
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    mul[0][0] = make_pair(false, '1');
    mul[0][1] = make_pair(false, 'i');
    mul[0][2] = make_pair(false, 'j');
    mul[0][3] = make_pair(false, 'k');

    mul[1][0] = make_pair(false, 'i');
    mul[1][1] = make_pair(true, '1');
    mul[1][2] = make_pair(false, 'k');
    mul[1][3] = make_pair(true, 'j');

    mul[2][0] = make_pair(false, 'j');
    mul[2][1] = make_pair(true, 'k');
    mul[2][2] = make_pair(true, '1');
    mul[2][3] = make_pair(false, 'i');

    mul[3][0] = make_pair(false, 'k');
    mul[3][1] = make_pair(false, 'j');
    mul[3][2] = make_pair(true, 'i');
    mul[3][3] = make_pair(true, '1');

    int test_cnt;
    cin >> test_cnt;

    for (int t = 0; t < test_cnt; t++) {
        int l, times;
        cin >> l >> times >> tmp;
        s = tmp;
        for (int i = 1; i < times; i++) {
            s += tmp;
        }
        n = l * times;
        if (n < 3) {
            //cerr << "Case #" << t + 1 << ": " << "NO" << "\n";
            cout << "Case #" << t + 1 << ": " << "NO" << "\n";
        }
        else {
            memset(sub_s_rez_char, 0, sizeof(sub_s_rez_char));
            memset(sub_s_rez_bool, 0, sizeof(sub_s_rez_bool));
            for (int L = 0; L < n; L++) {
                char cur_c = s[L];
                bool cur_minus = false;
                for (int R = L + 1; R <= n; R++) {

                    sub_s_rez_bool[L][R] = !(cur_minus);
                    sub_s_rez_char[L][R] = cur_c;
                    if (R < n) {
                        pair<bool, char> p = mul[c2int(cur_c)][c2int(s[R])];
                        cur_minus ^= p.first;
                        cur_c = p.second;
                    }
                }
            }
            cout << "Case #" << t + 1 << ": " << (get_ans() ? "YES":"NO") << "\n";
            //cerr << "Case #" << t + 1 << ": " << (get_ans() ? "YES":"NO") << "\n";
        }
    }
    return 0;
}
