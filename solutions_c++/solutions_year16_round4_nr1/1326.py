#include <bits/stdc++.h>

using namespace std;

const int X = (1 << 25);

char D[] = {0, 'P', 'S', 'R'};
char alph[X];

bool cmp(int s1, int f1, int s2, int f2) {
    while (s1 < f1 && s2 < f2) {
        if (alph[s1] < alph[s2]) {
            return true;
        }
        if (alph[s1] > alph[s2]) {
            return false;
        }
        s1++, s2++;
    }
    return true;
}

void sort_alph(int left, int right) {
    int middle = (left + right) / 2;
    if (!cmp(left, middle, middle, right)) {
        for (int i = 0; i + left < middle; i++) {
            swap(alph[i + left], alph[i + middle]);
        }
    }
}

void dfs(int n, int type, int left, int right) {
    if (n == 0) {
        alph[left] = D[type];
        return;
    }
    int middle = (left + right) / 2;
    if (type == 1) {
        dfs(n - 1, 1, left, middle);
        dfs(n - 1, 3, middle, right);
    } else if (type == 2) {
        dfs(n - 1, 2, left, middle);
        dfs(n - 1, 1, middle, right);
    } else {
        dfs(n - 1, 3, left, middle); 
        dfs(n - 1, 2, middle, right);
    }
    sort_alph(left, right);
}

void solution() {
    int n, r, p, s, new_r, new_p, new_s;
    cin >> n >> r >> p >> s;
    for (int i = n - 1; i >= 0; i--) {
        if (max(r, max(p, s)) > (1 << i)) {
            cout << "IMPOSSIBLE\n";
            return;
        }
        if (r >= p && r >= s) {
            new_p = p - (1 << i) + r;
            new_s = (1 << i) - r;
            new_r = r - new_p;
        } else if (s >= p && s >= r) {
            new_p = (1 << i) - s;
            new_r = r - (1 << i) + s;
            new_s = s - new_r;
        } else if (p >= s && p >= r){
            new_s = s - (1 << i) + p;
            new_r = (1 << i) - p;
            new_p = p - new_s;
        }
        p = new_p;
        s = new_s;
        r = new_r;
    }
    dfs(n, 1 * p + 2 * s + 3 * r, 0, (1 << n));
    for (int i = 0; i < (1 << n); i++) {
        cout << alph[i];
    }
    cout << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solution();
    }
    return 0;
}
