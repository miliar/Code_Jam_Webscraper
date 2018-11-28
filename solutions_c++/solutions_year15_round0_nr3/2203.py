#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
using namespace std;
typedef long long int ll;
typedef long double ld;

class Quaterion {
    public:
        const static int number_of_values = 8;
        enum possible_values { ONE=0, I=1, J=2, K=3, M_ONE=4, M_I=5, M_J=6, M_K=7};
        static int mul_result[4][4];
        Quaterion(possible_values val) : value(val){ }
        Quaterion(int val) : value(val){ }
        int value;
        int getSign() const  {
            if (value >= 4) {
                return -1;
            }
            return 1;
        }
};

int Quaterion::mul_result[4][4] = {
    {ONE, I, J, K},
    {I, M_ONE, K, M_J},
    {J, M_K, M_ONE, I},
    {K, J, M_I, M_ONE},
};

Quaterion operator-(const Quaterion q) {
    if (q.getSign() == -1) {
        return Quaterion(q.value - 4);
    }
    return Quaterion(q.value + 4);
}

Quaterion abs(const Quaterion q) {
    if (q.getSign() == -1) {
        return -q;
    }
    return q;
}

Quaterion operator*(const Quaterion lhs, const Quaterion rhs) {
    int sign = lhs.getSign() * rhs.getSign();
    int res = Quaterion::mul_result[abs(lhs).value][abs(rhs).value];
    Quaterion q = Quaterion(res);
    if (sign == -1) {
        return -q;
    }
    return q;
}

class CaseSolver {
    public:
        void static precompute();
        void read(istream& is);
        void solve();
        void write(ostream& os);
    private:
        int l;
        ll x;
        string text;
        const static int g_size = 24;
        static int g[3][g_size][g_size];
        int m[g_size][g_size];
        // matrix manipulation
        static void clear(int m[g_size][g_size]) {
            for (int i = 0; i < g_size; ++i) {
                for(int j = 0; j < g_size; ++j) {
                    m[i][j] = 0;
                }
            }
        }
        static void copy(int dest[g_size][g_size], int src[g_size][g_size]) {
            for (int i = 0; i < g_size; ++i) {
                for(int j = 0; j < g_size; ++j) {
                    dest[i][j] = src[i][j];
                }
            }
        }
        static void mul(int res[g_size][g_size], int lhs[g_size][g_size], int rhs[g_size][g_size]) {
            for (int i = 0; i < g_size; ++i) {
                for(int j = 0; j < g_size; ++j) {
                    res[i][j] = 0;
                    for (int k = 0; k < g_size; ++k) {
                        res[i][j] |= lhs[i][k] * rhs[k][j];
                    }
                }
            }
        }
        static void print(int m[g_size][g_size] ) {
            /*
            for ( int i = 0; i < g_size; ++i) {
                for (int j = 0; j < g_size; ++j) {
                    cout << setw(2) << "[" << i << "," << j << "]"<< m[i][j] << " ";
                }
                cout << "\n" << endl;
            }
            //*/
        }
};

int CaseSolver::g[3][g_size][g_size] = {};

void CaseSolver::precompute() {
    for (int z = 0; z < 3; ++z) {
        clear(g[z]);
    }
    for (int z = 0; z< 3; ++z) {
        Quaterion v(z+1);
        for(int i = 0; i < 3; ++i) {
            int pre = i * Quaterion::number_of_values;
            int looking_for;
            if (i == 0) {
                looking_for = Quaterion::I;
            } else if(i == 1) {
                looking_for = Quaterion::J;
            } else {
                looking_for = -1;
            }
            for (int j = 0; j < Quaterion::number_of_values; ++j) {
                Quaterion u(j);
                int res = (u*v).value;
                g[z][pre + j][pre + res] = 1;
                if (res == looking_for) {
                    g[z][pre + j][pre + Quaterion::number_of_values] = 1;
                }
            }
        }
        print(g[z]);
    }
}

void CaseSolver::read(istream& is) {
    is >> l >> x >> text;
}

void CaseSolver::solve() {
    clear(m);
    for (int i = 0; i < g_size; ++i) {
        m[i][i] = 1;
    }
    int res[g_size][g_size];
    copy(res, m);
    int tmp[g_size][g_size];
    for (int i = 0; i < l; ++i) {
        mul(tmp, m, g[text[i] - 'i']);
        copy(m, tmp);
    }
    while(x > 0) {
        if (x % 2 == 1) {
            mul(tmp, res, m);
            copy(res, tmp);
        }
        x /= 2;
        mul(tmp, m, m);
        copy(m, tmp);
    }
    copy(m, res);
    print (m);
}

void CaseSolver::write(ostream& os) {
    const string YES = "YES";
    const string NO = "NO";
    if (m[0][19]) {
        os << YES;
    } else {
        os << NO;
    }
}


int main() {
    CaseSolver::precompute();
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        CaseSolver caseSolver;
        caseSolver.read(cin);
        caseSolver.solve();
        cout << "Case #" << testCase << ": ";
        caseSolver.write(cout);
        cout << "\n";
	}
}
