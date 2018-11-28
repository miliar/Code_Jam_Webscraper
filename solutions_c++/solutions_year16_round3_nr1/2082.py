/*
 * Header file available here:
 * https://github.com/JosephConrad/GoogleCodeJam/tree/master/2016
 */
#include "../../template.h"


int findMax(std::vector<int> vector);

std::string solve(std::vector<int> parties) {
    std::string res = "";
    while (std::accumulate(parties.begin(), parties.end(), 0)  > 0)
    {
        int max_elem = 0;
        int max_i = 0;
        for (int i = 0; i < parties.size(); i++) {
            if (parties[i] > max_elem) {
                max_elem = parties[i];
                max_i = i;
            }
        }
        res += static_cast<char>(max_i + 65);
        parties[max_i] -= 1;
        if (std::accumulate(parties.begin(), parties.end(), 0)  == 2)
        {
            res += " ";
            continue;
        }
        else
        {
            int max_elem = 0;
            int max_i = 0;
            for (int i = 0; i < parties.size(); i++) {
                if (parties[i] > max_elem) {
                    max_elem = parties[i];
                    max_i = i;
                }
            }
            res += static_cast<char>(max_i + 65);
            parties[max_i] -= 1;
        }
        res += " ";
    }
    return res;
}

int findMax(std::vector<int> parties) {
    return 0;
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
        std::getline(std::cin, name);
        std::vector<int> parties = splitString<int, std::vector>(name);
        printf("Case #%d: %s\n", cc + 1, solve(parties).c_str());
    }
    fprintf(stderr, "*** Total time: %.3lf seconds ***\n",
            ((clock() - start) / (double) CLOCKS_PER_SEC));
    return 0;
}
