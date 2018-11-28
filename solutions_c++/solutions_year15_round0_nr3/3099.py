#include <iostream>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <functional>
#include <vector>
#include <cstdlib>
using namespace std;
struct Quad
{
    enum Lit { ONE, I, J, K };
    Quad() : lit(ONE), isNeg(false) {}
    explicit Quad(char x, bool neg = false) : lit(ONE), isNeg(neg) {
        switch(x) {
        case 'i':
        case 'I':
            lit = I;
            break;
        case 'j':
        case 'J':
            lit = J;
            break;
        case 'k':
        case 'K':
            lit = K;
            break;
        }
    }
    Quad(Lit l, bool neg = false) : lit(l), isNeg(neg) {}

    Quad& operator*=(const Quad& rhs)
    {
        if (rhs.isNeg) {
            isNeg = !isNeg;
        }
        switch(lit) {
        case ONE:
            lit = rhs.lit;
            return *this;
        case I:
            switch(rhs.lit) {
            case ONE:
                break;
            case I:
                lit = ONE;
                isNeg = !isNeg;
                break;
            case J:
                lit = K;
                break;
            case K:
                lit = J;
                isNeg = !isNeg;
                break;
            }
            break;
        case J:
            switch(rhs.lit) {
            case ONE:
                break;
            case I:
                lit = K;
                isNeg = !isNeg;
                break;
            case J:
                lit = ONE;
                isNeg = !isNeg;
                break;
            case K:
                lit = I;
                break;
            }
            break;
        case K:
            switch(rhs.lit) {
            case ONE:
                break;
            case I:
                lit = J;
                break;
            case J:
                lit = I;
                isNeg = !isNeg;
                break;
            case K:
                lit = ONE;
                isNeg = !isNeg;
                break;
            }
            break;
        }
        return *this;
    }

    Lit  lit;
    bool isNeg;
};

Quad operator*(const Quad& lhs, const Quad& rhs)
{
    Quad tmp(lhs);
    return tmp *= rhs;
}

bool operator==(const Quad& lhs, const Quad& rhs)
{
    if (lhs.lit != rhs.lit) return false;
    return ((lhs.isNeg && rhs.isNeg) || (!lhs.isNeg && !rhs.isNeg));
}

bool operator!=(const Quad& lhs, const Quad& rhs)
{
    return !(lhs == rhs);
}

Quad GET_RANGE(string::const_iterator beg, string::const_iterator end)
{
    Quad tmp(Quad::ONE);
    for (string::const_iterator i = beg; i != end; ++i)
    {
        tmp *= Quad(*i);
    }
    return tmp;
}

bool findIJK(const string &str)
{
    vector<Quad> fwd(str.length());
    bool hasI = false;
    Quad tmp(Quad::ONE);
    for (int j = 0; j < str.length(); ++j) {
        tmp *= Quad(str[j]);
        fwd[j] = tmp;
        if (tmp == Quad::I) hasI = true;
    }
    if (!hasI) return false;

    tmp = Quad::ONE;
    bool hasK = false;
    vector<Quad> bwd(str.length());
    for (int j = str.length() - 1; j >= 0; --j) {
        tmp = Quad(str[j]) * tmp;
        bwd[j] = tmp;
        if (tmp == Quad::K) hasK = true;
    }
    if (!hasK) return false;
    
    for (int i = 0; i < str.length(); ++i) {
        if (fwd[i] != Quad::I) continue;
        for (int j = str.length() - 1; j > i; --j) {
            if (bwd[j] != Quad::K) continue;
            if (GET_RANGE(str.begin()+i+1, str.begin()+j) == Quad::J)
                return true;
        }
    }
    return false;
}

int main(int argc, char ** argv)
{
    int T;
    cin >> T;
    int from, to;
    if (argc >= 3) {
        from = atoi(argv[1]);
        to = atoi(argv[2]);
    } else {
        from = 1;
        to = T;
    }
    for (int i = 1; i <= to; ++i) {
        int L, X;
        cin >> L >> X;
        string str;
        cin >> str;
        if (i < from) continue;
        cout << "Case #" << i << ": ";
        {
            ostringstream strm;
            for (int j = 0; j < X; ++j)
                strm << str;
            str = strm.str();
        }
        cout << (findIJK(str) ? "YES" : "NO") << endl;
    }
    return 0;
}
