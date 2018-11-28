#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long lint;

enum QKind { ONE, I, J, K };

struct QInt {
    int sign;
    QKind kind;

    QInt(QKind kind): sign(1), kind(kind) { }
    QInt(int sign, QKind kind): sign(sign), kind(kind) { }

    friend bool operator==(const QInt& a, const QInt& b) {
        return a.sign == b.sign && a.kind == b.kind;
    }

    friend bool operator!=(const QInt& a, const QInt& b) {
        return !(a == b);
    }

    friend ostream& operator<<(ostream& out, const QInt& a) {
        if (a.sign == -1) {
            out << "-";
        }
        if (a.kind == ONE) {
            out << "1";
        }
        else if (a.kind == I) {
            out << "i";
        }
        else if (a.kind == J) {
            out << "j";
        }
        else if (a.kind == K) {
            out << "k";
        }
        return out;
    }
};

const QInt QONE(ONE);
const QInt QMINUS_ONE(-1, ONE);
const QInt QI(I);
const QInt QK(K);

QInt multiply(QInt a, QInt b) {
    QInt res(a.sign * b.sign, ONE);
    if (a.kind == ONE) {
        res.kind = b.kind;
    }
    else if (b.kind == ONE) {
        res.kind = a.kind;
    }
    else if (a.kind == I) {
        if (b.kind == I) {
            res.kind = ONE;
            res.sign *= -1;
        }
        else if (b.kind == J) {
            res.kind = K;
        }
        else if (b.kind == K) {
            res.kind = J;
            res.sign *= -1;
        }
    }
    else if (a.kind == J) {
        if (b.kind == I) {
            res.kind = K;
            res.sign *= -1;
        }
        else if (b.kind == J) {
            res.kind = ONE;
            res.sign *= -1;
        }
        else if (b.kind == K) {
            res.kind = I;
        }
    }
    else if (a.kind == K) {
        if (b.kind == I) {
            res.kind = J;
        }
        else if (b.kind == J) {
            res.kind = I;
            res.sign *= -1;
        }
        else if (b.kind == K) {
            res.kind = ONE;
            res.sign *= -1;
        }
    }
    return res;
}

QInt power(QInt a, lint n) {
    QInt res = QONE;
    while (n > 0) {
        if (n % 2 == 1) {
            res = multiply(res, a);
        }
        a = multiply(a, a);
        n >>= 1;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int L;
        lint X;
        cin >> L >> X;
        cin.ignore();
        string raw_line;
        getline(cin, raw_line);
        vector< QInt > line;
        auto line_product = QONE;
        for (auto& c : raw_line) {
            QInt x(c == 'i' ? I : (c == 'j' ? J : K));
            line.push_back(x);
            line_product = multiply(line_product, x);
        }
        if (power(line_product, X) == QMINUS_ONE) {
            auto xs = line;
            for (int i = 1; i < X; ++i) {
                for (auto& x : line) {
                    xs.push_back(x);
                }
            }
            int i;
            QInt p = QONE;
            for (i = 0; p != QI && i < xs.size(); ++i) {
                p = multiply(p, xs[i]);
            }
            if (p == QI) {
                int i_len = i;
                reverse(xs.begin(), xs.end());
                p = QONE;
                for (i = 0; p != QK && i < xs.size(); ++i) {
                    p = multiply(xs[i], p);
                }
                if (p == QK) {
                    int k_len = i;
                    if (i_len + 1 + k_len <= L * X) {
                        cout << "YES";
                    }
                    else {
                        cout << "NO";
                    }
                }
                else {
                    cout << "NO";
                }
            }
            else {
                cout << "NO";
            }
        }
        else {
            cout << "NO";
        }
        cout << "\n";
    }
    return 0;
}
