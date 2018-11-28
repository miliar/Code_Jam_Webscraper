#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

struct Case {
    size_t A;
    size_t B;
};

std::vector<Case> readCases(std::istream& in)
{
    size_t N; 
    in >> N;
    std::vector<Case> cases;
    cases.reserve(N);
    for (size_t i = 0; i < N; ++i) {
        size_t A, B;
        in >> A >> B;
        cases.push_back(Case {A, B});
    }
    return cases;
}

bool ispol(size_t x)
{
    auto s = std::to_string(x);
    for (size_t i = 0, l = s.size(); i < l / 2; ++i)
        if (s[i] != s[l - 1 - i])
            return false;
    return true;
}

int main()
{
    size_t N = 1e7 + 1;
    std::vector<size_t> precalc;
    precalc.resize(N, 0);
    size_t counter = 0;
    for (size_t i = 0; i < N; ++i) {
        precalc[i] = counter;
        if (ispol(i) && ispol(i * i))
            counter++;
    }
    auto cases = readCases(std::cin);
    for (size_t i = 0; i < cases.size(); ++i) {
        const auto& c = cases[i];
        double ra = std::sqrt(c.A);
        double rb = std::sqrt(c.B);        
        size_t a = static_cast<size_t>(std::ceil(ra));
        size_t b = static_cast<size_t>(std::floor(rb));
        size_t n = (a <= b) ? precalc[b + 1] - precalc[a] : 0;
        std::cout << "Case #" << (i + 1) << ": " << n << std::endl; 
    }
    return 0;
}




