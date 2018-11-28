#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <utility>
#include <stdexcept>

using namespace std;

long long min(long long a, long long b) {
    return (a < b) ? a : b;
}

enum class QTYPE { ONE, I, J, K };
class Quat {
public:
    Quat(int sign, QTYPE qtype): sign{sign},qtype{qtype} { }
    bool operator==(const Quat& rhs) {
        return sign == rhs.sign && qtype == rhs.qtype;
    }
    bool operator!=(const Quat& rhs) {
        return !(*this == rhs);
    }

    int sign;
    QTYPE qtype;
};

Quat multiply(Quat q1, Quat q2) {
    int s = q1.sign * q2.sign;
    QTYPE qt;
    
    if (q1.qtype == QTYPE::ONE)
        qt = q2.qtype;
    else if (q2.qtype == QTYPE::ONE) {
        qt = q1.qtype; 
    }
    else if (q1.qtype == q2.qtype) {
        qt = QTYPE::ONE;
        s *= -1;
    }
    else if (q1.qtype == QTYPE::I && q2.qtype == QTYPE::J) {
        qt = QTYPE::K;
    }
    else if (q1.qtype == QTYPE::I && q2.qtype == QTYPE::K) {
        qt = QTYPE::J;
        s *= -1;
    } 
    else if (q1.qtype == QTYPE::J && q2.qtype == QTYPE::K) {
        qt = QTYPE::I;
    }
    else {
        return multiply(Quat(-1,q2.qtype), Quat(s,q1.qtype));
    }

    return Quat(s,qt);
}

Quat parse(char c) {
    if (c == 'i')
        return Quat(1,QTYPE::I);
    if (c == 'j')
        return Quat(1,QTYPE::J);
    if (c == 'k')
        return Quat(1,QTYPE::K);
    fprintf(stderr, "Bad character: %c\n", c);
    throw runtime_error {"parse failed"};
}

bool reducesToijk(const string &str, long long L, long long X) {
    // use fact that your 3 pieces will have lots of repetition  

    // One optimization: check if everything multiplies to -1
    {
    long long int q2 = X/4;
    long long int ub = X*L - q2*4*L;
    Quat optacc(1,QTYPE::ONE);
    for (int r = 0; r<ub; r++) {
        optacc = multiply(optacc, parse(str[r%L])); 
    }
    if (optacc != Quat(-1, QTYPE::ONE))
        return false;
    }

    // this is where the work really starts
    Quat leftacc(1,QTYPE::ONE);
    for (int r = 0; r < min(4*L,X*L); r++) {
        // test whether predicate reduces to i
        // simple O(1) update
        leftacc = multiply(leftacc, parse(str[r%L]));
        if (leftacc != Quat(1,QTYPE::I))
            continue;

        Quat midacc(1,QTYPE::ONE);
        for (int s = r+1; s < min(r + 4*L,X*L); s++) {
            // test middle expression
            midacc = multiply(midacc, parse(str[s%L]));
            if (midacc != Quat(1,QTYPE::J))
                continue;
            
            Quat rightacc(1,QTYPE::ONE);
            // third component must consume rest of input
            long long int q = (X*L - (s+1)) / (4*L);
            long long int upperbound = X*L - q*4*L;
            //for (int t = s+1; t < X*L; t++) { // TODO optimize upper bound later!
            for (int t = s+1; t < upperbound; t++) { // TODO optimize upper bound later!
                rightacc = multiply(rightacc, parse(str[t%L]));
            }
            if (rightacc == Quat(1,QTYPE::K)) {
                //cout << "(r,s) = (" << r << "," << s << ")\n";
                return true;
            }
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        long long L, X;
        string str;

        cin >> L >> X;    
        cin >> str;
        //assert(str.size() == L);
        //cout << str<< '\n';
        cout << "Case #" << t << ": ";
        if (reducesToijk(str, L, X))
            cout << "YES\n";
        else 
            cout << "NO\n";
    }
    return 0;
}
