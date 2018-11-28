// Yen-Ming Lee <leeym@leeym.com>
// http://HOST/codejam/contest/dashboard?c=6254486#s=pB
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <iostream>
#include <string>
using namespace std;
int verbose = 0, debug = 0;
std::string flip(std::string S)
{
    std::string D;
    for (int i = S.size() - 1; i >= 0; i--) {
        if (S[i] == '+') {
            D += '-';
        } else {
            D += '+';
        }
    }
    return D;
}
int main(int argc, char *argv[])
{
    int ch;
    while ((ch = getopt(argc, argv, "vd")) != -1) {
        switch (ch) {
        case 'v':
            verbose = 1;
            break;
        case 'd':
            debug = 1;
            break;
        }
    }
    argc -= optind;
    argv += optind;

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        fprintf(stderr, "Case #%d/%d\n", t, T);
        std::string S;
        cin >> S;
        int y = 0;
        while (S.find('-') != std::string::npos) {
            std::string S1;
            std::string S2;
            bool found = false;
            for (int i = 0; i < S.size(); i++) {
                if (found) {
                    S2 += S[i];
                } else {
                    if (S[i] == S[0]) {
                        S1 += S[i];
                    } else {
                        found = true;
                        S2 += S[i];
                    }
                }
            }
            if (verbose) fprintf(stderr, "\t(%s) (%s)\n", S1.c_str(), S2.c_str());
            S = flip(S1) + S2;
            if (verbose) fprintf(stderr, "\t%s\n", S.c_str());
            y++;
        }
        printf("Case #%d: %d\n", t, y);
        fflush(NULL);
    }
}
