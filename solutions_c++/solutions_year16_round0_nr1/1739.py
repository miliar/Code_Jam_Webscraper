#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdint>

#define TRACE(cmd)
//#define TRACE(cmd) cmd

typedef intmax_t Int;

std::string solve(Int n);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        Int n;
        std::cin >> n;
        std::cout << "Case #" << t << ": " << solve(n) << std::endl;
    }
    return 0;
}

std::string solve(Int N) {
    if (N == 0) {
        return "INSOMNIA";
    }

    bool found[10] = {false};
    bool allFound = false;
    Int cur = 0;
    do {
        cur += N;

        TRACE(std::clog << cur << std::endl);

        for (Int n = cur; n != 0; n/=10) {
            found[n%10] = true;
        }

        int i=0;
        for (i=0; i<10 && found[i]; ++i);
        allFound = (i == 10);
    } while(!allFound);

    std::stringstream r;
    r << cur;
    return r.str();
}


