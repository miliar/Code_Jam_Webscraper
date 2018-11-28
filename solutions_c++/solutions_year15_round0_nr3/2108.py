#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

char mulC[3][3] = {
        {'1', 'k', 'j'},
        {'k', '1', 'i'},
        {'j', 'i', '1'} };
bool mulN[3][3] = {
        {1, 0, 1},
        {1, 1, 0},
        {0, 1, 1} };

class quat {
public:
    bool mN;
    char mC;
    quat(bool n, char c) {
        mN = n;
        mC = c;
    }
    quat operator*(const quat &q) {
        bool n = mN ^ q.mN ^ mulN[mC - 'i'][q.mC - 'i'];
        if (mC == '1') {
            return quat(n, q.mC);
        } else if (q.mC == '1') {
            return quat(n, mC);
        } else {
            return quat(n, mulC[mC - 'i'][q.mC - 'i']);
        }
    }
    quat operator/(const quat &q) {
        bool n = mN ^ q.mN ^ mulN[q.mC - 'i'][mC - 'i'];
        if (mC == '1') {
            return quat(n, q.mC);
        } else if (q.mC == '1') {
            return quat(n, mC);
        } else {
            return quat(n, mulC[q.mC - 'i'][mC - 'i']);
        }
    }
    bool operator==(const quat &q) {
        return mC == q.mC && mN == q.mN;
    }
};

std::ostream& operator<< (std::ostream& os, const quat& q) {
    return os << (q.mN ? '-' : '+') << q.mC;
}

quat I(0, 'i');
quat J(0, 'j');
quat K(0, 'k');

int l, x;
vector<quat> str;

int main() {
    ifstream cin("src/in.txt");
    ofstream cout("src/out.txt");
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        //
        str.clear();
        string s;
        cin >> l >> x >> s;
        for (int j = 0; j < x; ++j) {
            for (int k = 0; k < l; ++k) {
                str.push_back(quat(0, s[k]));
            }
        }
        //
        vector<quat> pre;
        pre.push_back(str[0]);
        for (int j = 1; j < str.size(); ++j) {
            pre.insert(pre.end(), pre[j - 1] * str[j]);
        }
        //
        vector<quat> post;
        post.push_back(str[str.size() - 1]);
        for (int j = str.size() - 2; j >= 0; --j) {
            post.insert(post.begin(), str[j] * post[0]);
        }
        //
        bool done = false;
        for (int j = 0; j < str.size() && !done; ++j) {
            if (pre[j] == I)
                for (int k = str.size() - 1; k > j + 1 && !done; --k) {
                    if (post[k] == K) {
                        done = (post[j + 1] / post[k]) == J;
                    }
                }
        }
        //
        cout << "Case #" << (i + 1) << ": " << (done ? "YES" : "NO") << endl;
    }
}
