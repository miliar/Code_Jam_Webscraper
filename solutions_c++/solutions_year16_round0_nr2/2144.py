#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;

std::string S;

bool done(const std::string &S) {
    for(int i = 0; i < S.size(); ++i)
        if(S[i] == '-') return false;
    return true;
}

std::string flip(const std::string &S)
{
    std::string res;
    for(int i = 0; i < S.size(); ++i)
        res += (S[i] == '+') ? '-' : '+';
    return res;
}

int rec(std::string str) {
    // std::cout << str << std::endl;
    if(done(str)) return 0;

    int start = 0;
    while(start < str.size() && str[start] != '+') ++start;
    if(start && start != str.size()) {
        str = flip(str.substr(0, start)) + str.substr(start);
    }
    str = flip(str);
    int far = str.size() - 1;
    while(far >= 0 && str[far] == '+') --far;
    
    // std::cout << str << " " << far << std::endl;

    return rec(str.substr(0, far + 1)) + 1 + ((start && start != str.size()) ? 1 : 0);
}

int solve() {
    int far = S.size() - 1;
    while(far >= 0 && S[far] == '+') --far;

    return rec(S.substr(0, far + 1));
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
