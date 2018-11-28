#include <cstring>
#include <iostream>
using namespace std;
#define LXMAX 10100



int TC, L, X;
char str[LXMAX];

struct quat {
    char s;
    bool n;
    quat() {}
    quat(char s, bool n) : s(s), n(n) {}
    quat operator*(const quat &q) const;
    quat operator*(const char &a) const {
        return *this * quat(a, 0);
    }
    bool operator==(const quat &q) const {
        return (s == q.s) && (n == q.n);
    }
};

quat aim[] = {quat('i',0), quat('j',0), quat('k',0)};
quat table[4][4] = {{quat('1',0), quat('i',0), quat('j',0), quat('k',0)},
                    {quat('i',0), quat('1',1), quat('k',0), quat('j',1)},
                    {quat('j',0), quat('k',1), quat('1',1), quat('i',0)},
                    {quat('k',0), quat('j',0), quat('i',1), quat('1',1)}};

quat quat::operator*(const quat &q) const {
    int r, c;
    switch (s) {
        case '1': r = 0; break;
        case 'i': r = 1; break;
        case 'j': r = 2; break;
        case 'k': r = 3; break;
    }
    switch (q.s) {
        case '1': c = 0; break;
        case 'i': c = 1; break;
        case 'j': c = 2; break;
        case 'k': c = 3; break;
    }
    return quat(table[r][c].s, n^q.n^table[r][c].n);
}


bool cached[LXMAX];
quat cache[LXMAX];
quat dfs22(int i) {
    if (i == L*X-1) return quat(str[i%L], 0);
    if (cached[i]) return cache[i];
    cache[i] = quat(str[i%L], 0) * dfs22(i+1);
    cached[i] = 1;
    return cache[i];
}
bool dfs2(int start) {
    if (dfs22(start) == aim[2] ) return true;
    return false;
    //
    quat cur = quat('1',0);
    for (int i = start; i < L*X; ++i) {
        cur = cur * str[i%L];
    }
    if (cur == aim[2] ) return true;
    return false;
}

bool dfs1(int start) {
    quat cur = quat('1',0);
    for (int i = start; i < L*X-1; ++i) {
        cur = cur * str[i%L];
        if (cur == aim[1] && dfs2(i+1) ) return true;
    }
    return false;
}

bool dfs0() {
    quat cur = quat('1',0);
    for (int i = 0; i < L*X-2; ++i) {
        cur = cur * str[i%L];
        /* cout << (cur.n ? "-":"") << cur.s << endl; */
        if (cur == aim[0] && dfs1(i+1) ) return true;
    }
    return false;
}



int main() {
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        cin >> L >> X;
        cin >> str;
        memset(cached, 0, sizeof(cached));
        cout << "Case #" << tc << ": " << (dfs0() ? "YES":"NO") << endl;
    }
    return 0;
}
