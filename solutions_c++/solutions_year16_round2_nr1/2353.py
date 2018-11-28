#include <iostream>
#include <array>
#include <string>
#include <cassert>

std::string solve(std::string const& in)
{
    std::array<size_t, 26> hist;
    hist.fill(0);

    for (auto c : in) {
        ++hist.at(c - 'A');
    }

    auto count = [&](char c, std::string name) {
        auto k = hist.at(c - 'A');
        for (auto c : name) {
            hist.at(c - 'A') -= k;
        }
        return k;
    };

    std::array<size_t, 10> out;
    out.fill(0);

    out[0] = count('Z', "ZERO");
    out[2] = count('W', "TWO");
    out[6] = count('X', "SIX");
    //
    out[7] = count('S', "SEVEN");
    out[5] = count('V', "FIVE");
    out[4] = count('F', "FOUR");
    out[8] = count('G', "EIGHT");
    out[3] = count('R', "THREE");
    out[1] = count('O', "ONE");
    out[9] = count('I', "NINE");

    for (auto c : hist) {
        assert(c == 0);
    }

    std::string ret;
    for (int d = 0; d <= 9; ++d) {
        ret += std::string(out[d], '0' + d);
    }

    return ret;
}

int main()
{
    size_t N;
    std::cin >> N;

    for (size_t i = 1; i <= N; ++i) {
        std::string s;
        std::cin >> s;
        std::cout << "Case #" << i << ": " << solve(s) << std::endl;
    }
}
