#include "bits/stdc++.h"

unsigned int swap(unsigned int N) {
    std::string s = std::to_string(N);
    return std::stoi(std::string(s.rbegin(), s.rend()));
}

unsigned int solve(unsigned int N) {
    std::unordered_set<unsigned int> H;
    std::queue<std::pair<unsigned int, unsigned int> > Q;
    std::pair<unsigned int, unsigned int> x(1, 1);
    if (x.first == N) {
        return x.second;
    }
    if (H.find(x.first) == H.end()) {
        Q.push(x);
        H.emplace(x.first);
    }
    while (!Q.empty()) {
        x = Q.front();
        std::pair<unsigned int, unsigned int> u(x.first + 1, x.second + 1);
        if (u.first == N) {
            return u.second;
        }
        if (H.find(u.first) == H.end()) {
            Q.push(u);
            H.emplace(u.first);
        }
        std::pair<unsigned int, unsigned int> v(swap(x.first), x.second + 1);
        if (v.first == N) {
            return v.second;
        }
        if (H.find(v.first) == H.end()) {
            Q.push(v);
            H.emplace(v.first);
        }
        Q.pop();
    }
    return 0;
}

int main() {
    unsigned int T = 0;
    std::cin >> T;
    for (unsigned int x = 1; x <= T; ++x) {
        unsigned int N = 0;
        std::cin >> N;
        std::cout << "Case #" << x << ": " << solve(N) << std::endl;
    }
    return 0;
}
