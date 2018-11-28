// Boost libraries available from www.boost.org 
#include <boost/lexical_cast.hpp>
using boost::lexical_cast;
#include <boost/format.hpp>

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

#define qq << " " <<
typedef double Int;

int T;
double C, F, X;
typedef vector<Int> vt;
vt A(20);
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
double ans()
{
    double ttf = X / 2 ;
    double ttb = C / 2;
    double ovh = 0.0;

    for(int i = 1;; ++i) {
        auto nttf = X / (2 + i*F);
        auto ttbf = ttb + nttf;
       // cerr qq ttf qq ttb qq ovh qq ttbf << endl;
        if (ttf <= ttbf) return ovh + ttf;
        ovh += ttb;
        ttf = nttf;
        ttb = C / (2 + i*F);
    }

    return 0.0;
}

string answer()
{
   return boost::str(boost::format("%0.7f") % ans());
}

int main(int argc, char** argv)
{
    cin >> T;

    string junk;
    for (testcase = 1; testcase <= T; ++testcase) {
        cin >> C >> F >> X ;
        cout << "Case #" << testcase << ": "
            << answer() << endl;

    }
}
