#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cstdint>

int64_t solve(int64_t , const std::vector<int64_t>& audience) {
    int64_t alreadyStanding = audience[0];
    int64_t friends = 0;

    for (size_t i = 1; i != audience.size(); ++i) {
        if (audience[i] == 0)
            continue;

        if ((int64_t)i <= alreadyStanding) {
            alreadyStanding += audience[i];
        } else {
            friends += (i - alreadyStanding);
            alreadyStanding += (i - alreadyStanding) + audience[i];
        }
    }
    return friends;
}

std::vector<int64_t> parseAudience(const std::string& input) {
    std::vector<int64_t> out;
    for (const auto& c : input) {
        out.push_back(c-'0');
    }
    return out;
}

void test() {
    auto a = parseAudience("1109");
    assert(a[0] == 1);
    assert(a[1] == 1);
    assert(a[2] == 0);
    assert(a[3] == 9);
    
    assert(solve(4, {1,1,1,1,1}) == 0);
    assert(solve(1, {0,9}) == 1);
    assert(solve(5, {1,1,0,0,1,1}) == 2);
    assert(solve(0, {1}) == 0);
}

int main() {
    test();
    size_t T;
    std::cin >> T;
    for (size_t i = 0; i != T; ++i) {
        int64_t max;
        std::string audienceRaw;
        std::cin >> max >> audienceRaw;
        auto audience = parseAudience(audienceRaw);
        std::cout << "Case #" << (i+1) << ": " << solve(max, audience) << std::endl;
    }
}
