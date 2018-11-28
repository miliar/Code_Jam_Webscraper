#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
#include <vector>
#include <cstdio>
#include <cstdint>
#include <sstream>
#include <cmath>

using namespace std;

#define RELEASE

#ifndef RELEASE
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...)
#endif

int main(int argc, char** argv) {
    // Comment this out to use as: [exe] < input.in
    //freopen("input.in", "r", stdin);

    int T;
    cin >> T;
    cin.ignore();
    debug("T = %d\n", T);

    for (int TC=1; TC <= T; ++TC) {
        string line;
        getline(cin, line);
        debug("Testcase %d: %s\n", TC, line.c_str());

        int pos = line.find_first_of(" ");
        debug("pos %d\n", pos);
        string maxSstring = line.substr(0, pos);
        int maxS = atoi(maxSstring.c_str());
        debug("  maxS: %d\n", maxS);

        int peopleStanding = 0;
        int solution = 0;

        for (int i=0; i <= maxS; ++i) {
            int n = line[i+pos+1]-0x30;

            int friends = 0;
            if (peopleStanding < i && n > 0) {
                friends = (i-peopleStanding);
            }
            peopleStanding += n + friends;
            solution += friends;

            debug("  %d: %d - peopleStanding %d, solution %d\n", i, n, peopleStanding, solution);
        }

        printf("Case #%d: %d\n", TC, solution);
    }

    return 0;
}