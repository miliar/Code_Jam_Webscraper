// Compiled with gcc in Ubuntu 16.04 with c++11 features.

#include <stdint.h>

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

struct combs {
    int r;
    int p;
    int s;
};

int main (int, char*[])
{
    std::vector<combs> comb(13);

    comb[0] = combs{1, 0, 0};
    for (int i = 1; i < 13; i++) {
        comb[i] = {comb[i-1].r + comb[i-1].p, comb[i-1].p + comb[i-1].s, comb[i-1].s + comb[i-1].r};
    }

    int num_of_cases;
    std::cin >> num_of_cases;
    std::string str;
    std::getline(std::cin, str);

    for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
        std::cout << "Case #" << case_num << ": ";
        int n, r, p, s;
        std::cin >> n >> r >> p >> s;

        std::string result;
        if (r == comb[n].r && p == comb[n].p && s == comb[n].s)
            result = "R";
        else if (r == comb[n].p && p == comb[n].s && s == comb[n].r)
            result = "S";
        else if (r == comb[n].s && p == comb[n].r && s == comb[n].p)
            result = "P";
        else {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        std::vector<std::string> r_s(13), p_s(13), s_s(13);
        r_s[0] = "R";
        p_s[0] = "P";
        s_s[0] = "S";
        for (int i = 1; i <= n; i++) {
            r_s[i] = std::min(r_s[i-1] + s_s[i-1], s_s[i-1] + r_s[i-1]);
            s_s[i] = std::min(s_s[i-1] + p_s[i-1], p_s[i-1] + s_s[i-1]);
            p_s[i] = std::min(p_s[i-1] + r_s[i-1], r_s[i-1] + p_s[i-1]);
        }

        cout << ((result == "R") ? r_s[n] : (result == "S" ? s_s[n] : p_s[n]))
             << endl;
    }

    return 0;
}