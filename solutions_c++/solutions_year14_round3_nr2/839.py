#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <memory>
#include <thread>
#include <numeric>
#include <future>
#include <limits>
#include <map>
#include <set>

bool is_good(const std::vector<std::string>& words, const std::vector<size_t>& positions)
{
    char c = 0;
    char nc = 0;
    std::set<char> S{0};
    for (size_t i = 0; i < positions.size(); ++i) {
        for (auto wc: words[positions[i]]) {
            nc = wc;
            if (nc != c) {
                if (S.count(nc)) {
                    return false;
                } else {
                    c = nc;
                    S.insert(c);
                }
            }
        }
    }
    return true;
}

uint64_t count(const std::vector<std::string>& words)
{
    uint64_t counter = 0;
    std::vector<size_t> pos(words.size());
    for (size_t i = 0; i < pos.size(); ++i)
        pos[i] = i;
    
    do {
        if (is_good(words, pos)) {
            counter += 1;
        }
    } while(std::next_permutation(pos.begin(), pos.end()));
    return counter % 1000000007;
}
 
int main()
{
    auto& in = std::cin;
    auto& out = std::cout;

    size_t T;
    in >> T;
    for (size_t t = 0; t < T; ++t) {
        size_t L;
        in >> L;
        std::vector<std::string> words;
        for (size_t i = 0; i <L; ++i) {
            std::string w;
            in >> w;
            words.push_back(w);
        }
        out << "Case #" << (t + 1) << ": " << count(words) << std::endl;
    }

    return 0;
}

