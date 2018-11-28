/*
 * Header file available here:
 * https://github.com/JosephConrad/GoogleCodeJam/tree/master/2016
 */
#include "../../template.h"


int solve(std::vector<char> pancakes) {
    int changes = 0;
    char previous = pancakes[0];
    for (int i = 1; i < pancakes.size(); i++) {
        if (pancakes[i] != previous) {
            changes++;
            previous = pancakes[i];
        }
    }
    if (pancakes.back() == '-') {
        changes++;
    }
    return changes;
}


int main() {

#ifndef GOOGLE_CODE_JAM
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    clock_t start = clock();

    std::string name;
    std::getline(std::cin, name);
    int T = std::stoi(name);
    REP(cc, T) {
        std::getline(std::cin, name);
        std::vector<char> pancakes = splitString<char, std::vector>(name);
        printf("Case #%d: %d\n", cc + 1, solve(pancakes));
    }
    fprintf(stderr, "*** Total time: %.3lf seconds ***\n",
            ((clock() - start) / (double) CLOCKS_PER_SEC));
    return 0;
}
