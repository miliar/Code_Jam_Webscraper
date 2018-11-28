#include <iostream>
#include <vector>
#include <string>

using namespace std;

class quaternion {
public:
    bool pos;
    char val;
    quaternion() {
        pos = true;
        val = '1';
    }
    explicit quaternion(char c) {
        pos = true;
        val = c;
    }
    quaternion(bool pos, char c) {
        this->pos = pos;
        val = c;
    }
    int valind() const {
        switch (this->val) {
            default:
            case '1':
                return 0;
            case 'i':
                return 1;
            case 'j':
                return 2;
            case 'k':
                return 3;
        }
    }
};

quaternion operator*(const quaternion &l, const quaternion &r) {
    int mat[4][4] = {
        {'1', 'i', 'j', 'k'},
        {'i', '1', 'k', 'j'},
        {'j', 'k', '1', 'i'},
        {'k', 'j', 'i', '1'}
    };
    int pos[4][4] = {
        { true, true, true, true },
        { true, false, true, false },
        { true, false, false, true },
        { true, true, false, false }
    };
    int newval = mat[l.valind()][r.valind()];
    int newpos = pos[l.valind()][r.valind()];
    if (l.pos != r.pos) newpos = !newpos;
    return quaternion(newpos, newval);
}

ostream &operator<<(ostream &o, const quaternion &q) {
    if (!q.pos) o << '-';
    o << q.val;
    return o;
}

void doit() {
    int L, X;
    cin >> L >> X;

    string S;
    cin >> S;

    quaternion qS, cur;
    int part = 0;
    int mode = 0;
    /* 0 = search i,
     * 1 = j
     * 2 = k
     */

    for (auto si: S) qS = qS * quaternion(si);

    for (part = 0; part < min(5, X) && mode < 2; ++part) {
        for (int i = 0; i < S.size(); ++i) {
            cur = cur * quaternion(S[i]);
            //cout << "cur: " << cur << endl;
            switch (mode) {
                case 0:
                    if (cur.val == 'i' && cur.pos) { mode++; cur = quaternion(); }
                    break;
                case 1:
                    if (cur.val == 'j' && cur.pos) { mode++; cur = quaternion(); }
                    break;
            }
        }
    }

    if (mode != 2) {
        cout << "NO" << endl;
        return;
    }

    int other_parts = (X - part) % 4;
    for (int i = 0; i < other_parts; ++i) {
        cur = cur * qS;
    }
    if (cur.val == 'k' && cur.pos) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) { cout << "Case #" << i << ": "; doit(); }
    return 0;
}
