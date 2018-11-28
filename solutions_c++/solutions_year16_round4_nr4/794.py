#include <iostream>
#include <string>

using namespace std;

int n, ans;
string s;
bool b[4][4], ok;
int p[4], m[4];

void try_to_choose(int k) {
    if (k == n)
        return;

    int i = p[k];
    bool flag = false;
    for (int j = 0; j < n; j++) {
        if (b[i][j] && m[j] == -1) {
            flag = true;
            m[j] = i;
            try_to_choose(k+1);
            m[j] = -1;
        }
    }

    if (!flag)
        ok = false;
}

void try_to_teach(int i, int j, int cnt) {

    if (i == n) {
        for (int k = 0; k < n; k++)
            p[k] = k;
        ok = true;
        do {
            memset(m, 0xff, sizeof m);
            try_to_choose(0);

            if (!ok)
                break;
        } while (next_permutation(p, p + n));

        if (ok && ans > cnt)
            ans = cnt;

        return;
    }

    int ni = i;
    int nj = j + 1;
    int ncnt = cnt + 1;
    if (nj == n) {
        ni++;
        nj = 0;
    }

    if (b[i][j])
        try_to_teach(ni, nj, cnt);
    else {
        b[i][j] = true;
        try_to_teach(ni, nj, ncnt);
        b[i][j] = false;
        try_to_teach(ni, nj, cnt);
    }
}

int main() {
    int t;

    ios::sync_with_stdio(0);

    cin >> t;
    for (int case_no = 1; case_no <= t; case_no++) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> s;
            for (int j = 0; j < n; j++)
                b[i][j] = s[j] == '1';
        }

        ans = 1000;
        try_to_teach(0, 0, 0);

        cout << "Case #" << case_no << ": " << ans << endl;
    }

    return 0;
}