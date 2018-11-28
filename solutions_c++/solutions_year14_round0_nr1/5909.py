// Boost libraries available from www.boost.org 
#include <boost/lexical_cast.hpp>
using boost::lexical_cast;

#include <iomanip>
#include <string>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <memory>
#include <map>
#include <list>
#include <bitset>
#include <cstring>

using namespace std;


typedef int Int;

Int T;
Int a, b;
typedef vector<Int> vt;
vt A(4), B(4);
Int testcase;


ostream& operator<<(ostream& os, const vt& v) 
{
    for (size_t i = 0; i < v.size(); ++i) {
        if (i) os << " ";
        os << v[i];
    }
    return os;
}

Int sum(vt& S)
{
    Int s = 0;
    for (size_t i =0; i < S.size(); ++i) {
        s += S[i];
    }
    return s;
    
}


string answer()
{
    Int ans = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j<4; ++j) {
            if (A[i] == B[j]) {
                if (ans) return "Bad magician!";
                ans = A[i];
            }
        }

    if (ans) return lexical_cast<string>(ans);
    return "Volunteer cheated!";
}

int main(int argc, char** argv)
{
    cin >> T;

    string junk;
    for (testcase = 1; testcase <= T; ++testcase) {
        //cerr << "\nTest case: " << testcase << endl;
        //A.clear();
        cin >> a  ;
        // cerr << "a: " << a << endl;
        for (int i = 0 ; i < 16 ; ++ i) {
            Int tmp;
            cin >> tmp;
            // cerr << "read: " << tmp << endl;
            if (i/4 != a -1) continue;
            // cerr << "adding: " << tmp << endl;
            A[i % 4] = tmp ;
        }
        // cerr << A << "----" << B << endl;
        //B.clear();
        cin >> b  ;
        for (int i = 0 ; i < 16 ; ++ i) {
            Int tmp;
            cin >> tmp;
            if (i/4 != b -1) continue;
            B[i % 4] = tmp ;
        }
        // cerr << A << "----" << B << endl;
        cout << "Case #" << testcase << ": "
            << answer() << endl;

    }
}
