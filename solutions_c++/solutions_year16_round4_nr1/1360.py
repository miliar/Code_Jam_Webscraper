#include <iostream>
#include <algorithm>
#include <string>
#include <cassert>
using std::string;

bool relax(int p, int r, int s, string& res) {
    if (p < 0 || r < 0 || s < 0) return false;
    if (p + r + s == 1) {
        if (p) res.push_back('P');
        if (r) res.push_back('R');
        if (s) res.push_back('S');
        return true;
    }
    int p1 = (r+p-s)/2;
    int r1 = (s+r-p)/2;
    int s1 = (p+s-r)/2; int dp = p-p1, dr = r-r1, ds = s-s1;
    if (!relax(p1, r1, s1, res)) return false;
    int sz = res.size();
    res.resize(2*sz);
    for (int i = sz-1; i >= 0; i--) {
        res[i*2+1] = res[i];
        if (res[i] == 'P')
            res[i*2] = 'R';
        else if (res[i] == 'S')
            res[i*2] = 'P';
        else if (res[i] == 'R')
            res[i*2] = 'S';
    }
    return true;
}

int main() {
    int T, N, R, P, S, n_case = 1;
    std::cin >> T;
    while (T--) {
        std::cin >> N >> R >> P >> S;
        std::cout << "Case #" << n_case++ << ": ";
        std::string res;
        if (!relax(P, R, S, res))
            std::cout << "IMPOSSIBLE" << std::endl;
        else {
            int w = 1;
            for (; w < res.size(); w *= 2) {
                for (int i = 0; i < res.size(); i+=2*w) {
                    if (res.substr(i, w) > res.substr(i+w, w))
                        std::swap_ranges(res.begin()+i, res.begin()+i+w, res.begin()+i+w);
                }
            }
            std::cout << res << std::endl;
        }
    }

    return 0;
}
