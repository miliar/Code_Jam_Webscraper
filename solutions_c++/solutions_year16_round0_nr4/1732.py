#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdint>
#include <vector>

//typedef __int128 Int;
typedef intmax_t Int;

//*
#define TRACE(cmd)
//*/

/*
#define DO_TRACE
#define TRACE(cmd) std::clog << cmd << std::endl
//*/

std::string solve_small(int k, int c, int s);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        int k, c, s;
        std::cin >> k >> c >> s;
        std::cout << "Case #" << t << ": " << solve_small(k, c, s) << std::endl;
    }
    return 0;
}

Int qpow(Int i, Int k) {
    if (k == 0) return 1;
    if (k == 1) return i;
    Int ret = qpow(i, k/2);
    ret *= ret;
    if (k&1) ret *= i;
    return ret;
}

std::string solve_small(int k, int c, int s) {
    // if (k != s) return "IMPOSSIBLE";
    // this is only for small set
    if (s < k)
        return "IMPOSSIBLE";

    std::stringstream ret;
    Int val = 0;
    Int inc = qpow(k, c-1);
    for (int i=0; i<k; i++) {
        ret << (val+1) << " ";
        val += inc;
    }
    std::string r = ret.str();
    r.pop_back();
    return r;
}

/*
GGGGGGGG
GGGGGGGL
LGGGGGGG
LLLLLLLL

GGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGL
LGGGGGGGGGGGGGGG
LLLLLLLLLLLLLLLL

*/


