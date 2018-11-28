#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;

int N;

bool seen[11];
int solve() {
    if(!N) return -1;
    memset(seen, false, sizeof(seen));

    int cur = N;
    while(true) {
        int temp = cur;
        while(temp) {
            seen[temp % 10] = true;
            temp /= 10;
        }
        for(int i = 0; i < 10; ++i)
            if(!seen[i]) goto loop;
        return cur;
loop:;
        cur += N;
    }
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N;

        int sol = solve();
        std::string ans = (sol == -1) ? "INSOMNIA" : std::to_string(sol);
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }

    return 0;
}
