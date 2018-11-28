#include <cstdio>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <utility>
#include <numeric>
#include <set>
#include <map>
#include <string>
#include <cstring>

typedef long long ll;
typedef std::pair<int, int> pii;

std::string S;
const int MAX = 22222;

std::string rem(const std::string & s, int & tot, bool & del) {
    std::string nxt = "";
    del = false;
    for(int i = 0; i < S.size(); ) {
        if(S[i] == S[i + 1]) {
            tot += 10;
            i += 2;
            del = true;
        } else {
            nxt += S[i];
            ++i;
        }
    }
    return nxt;
}

int solve() {
    int res = 0;
    bool del = true;
    while(del) {
        S = rem(S, res, del);
    }

    return res + 5 * S.size() / 2;
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> S; 

        int ans = solve();
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
    return 0;
}

