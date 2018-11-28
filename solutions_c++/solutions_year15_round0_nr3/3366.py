#include "iostream"
#include <vector>

using namespace std;

struct Quat {
        int base;
        int sign;

        bool operator!=(const Quat &rhs) const {
                return (base != rhs.base || sign != rhs.sign);
        }
        bool operator==(const Quat &rhs) const {
                return (base == rhs.base && sign == rhs.sign);
        }
};

enum QUAT_STATES {Q1 = 0, QI = 1, QJ = 2, QK = 3};

Quat qmul(const Quat &l, const Quat &r) {
        int sign = l.sign * r.sign;
        if (l.base == Q1) {
                return Quat {r.base, sign};
        }
        if (r.base == Q1) {
                return Quat {l.base, sign};
        }
        if (l.base == QI) {
                if (r.base == QI) {
                        return Quat {Q1, -sign };
                }
                if (r.base == QJ) {
                        return Quat {QK, sign };
                }
                if (r.base == QK) {
                        return Quat {QJ, -sign };
                }
        }
        if (l.base == QJ) {
                if (r.base == QI) {
                        return Quat {QK, -sign };
                }
                if (r.base == QJ) {
                        return Quat {Q1, -sign };
                }
                if (r.base == QK) {
                        return Quat {QI, sign };
                }
        }
        if (l.base == QK) {
                if (r.base == QI) {
                        return Quat {QJ, sign };
                }
                if (r.base == QJ) {
                        return Quat {QI, -sign };
                }
                if (r.base == QK) {
                        return Quat {Q1, -sign };
                }
        }
}

Quat qinv(const Quat &x) {
        if (x.base == Q1) {
                return Quat {Q1, x.sign};
        }
        return Quat {x.base, -x.sign};
}

Quat char2Quat(char &c) {
        if (c == 'i') {
                return Quat {QI, 1 };
        }
        if (c == 'j') {
                return Quat {QJ, 1 };
        }
        if (c == 'k') {
                return Quat {QK, 1 };
        }
}

Quat quatPow(const Quat &x, int exp) {
        Quat result = Quat {Q1, 1};
        for (int i = 0; i < (exp % 4); ++i) {
                result = qmul(result, x);
        }
        return result;
}



int main() {
        int T;
        cin >> T;
        for (int t = 1; t <= T; ++t) {
                bool possible = false;
                int L, X;
                cin >> L >> X;
                vector<Quat> s;
                s.reserve(L);
                vector<Quat> s_eval;
                s_eval.reserve(L+1);
                s_eval.push_back(Quat {Q1, 1});
                for (int l = 0; l < L; ++l) {
                        char c;
                        cin >> c;
                        s.push_back(char2Quat(c));
                        s_eval.push_back(qmul(s_eval[l], s[l]));
                }
                if (quatPow(s_eval[L], X) != Quat {Q1, -1}) {
                        possible = false;
                        goto print_solution;
                }

                for (int i1 = 0; i1 < min(4, X-1); ++i1) {
                        for (int l1 = 0; l1 < L; ++l1) {
                                if (qmul( quatPow(s_eval[L], i1), s_eval[l1]) == Quat {QI, 1}) {
                                        Quat rem = qmul(qinv(s_eval[l1]), s_eval[L]);
                                        for (int i2 = 0; i2 < min(4, X - i1 - 1); ++i2) {
                                                for (int l2 = 0; l2 < L; ++l2) {
                                                        if(qmul(rem, qmul(quatPow(s_eval[L], i2), s_eval[l2])) == Quat {QJ, 1}) {
                                                                possible = true;
                                                                goto print_solution;
                                                        }
                                                }
                                        }
                                        break;
                                }
                        }
                }
                for (int i1 = 0; i1 < min(4, X); ++i1) {
                        for (int l1 = 0; l1 < L; ++l1) {
                                if (qmul( quatPow(s_eval[L], i1), s_eval[l1]) == Quat {QI, 1}) {
                                        Quat rem = qmul(qinv(s_eval[l1]), s_eval[L]);
                                        for (int l2 = l1+1; l2 < L; ++l2) {
                                                if (qmul(qinv(s_eval[l1]), s_eval[l2]) == Quat {QJ, 1}) {
                                                        possible = true;
                                                        goto print_solution;
                                                }
                                        }
                                        break;
                                }
                        }
                }
                
print_solution:
                cout << "Case #" << t << ": ";
                if (possible) {
                        cout << "YES";
                } else {
                        cout << "NO";
                }
                cout << endl;
        }
        return 0;
}
