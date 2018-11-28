#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <iostream>
#include <cstdint>

struct q {
    q(const char c, const bool negative = false) : c(c), negative(negative) {
        assert(c == '1' || c == 'i' || c == 'j' || c == 'k');
    }

    q operator * (const q& rhs) {
        static char tab[] = "1ijki1kjjk1ikji1";
        int offset = toIndex(c)*4 + toIndex(rhs.c);
        bool neg = givesNegative(rhs.c);
        if (negative != rhs.negative) {
            neg = !neg;
        }
        return q(tab[offset], neg);
    }

    q& operator *= (const q& rhs) {
        static char tab[] = "1ijki1kjjk1ikji1";
        const int offset = toIndex(c)*4 + toIndex(rhs.c);
        const bool neg = givesNegative(rhs.c);
        c = tab[offset];
        negative = (negative != rhs.negative) ? !neg : neg;
        return *this;
    }

    bool operator == (const q& rhs) {
        return c == rhs.c && negative == rhs.negative;
    }

    bool operator != (const q& rhs) {
        return !(*this == rhs);
    }

private:
    int toIndex(const char c) {
        switch (c) {
            case '1' : return 0;
            case 'i' : return 1;
            case 'j' : return 2;
            case 'k' : return 3;
        }
    }

    bool givesNegative(const char rhsc) const {
        if (c == 'i') {
            return (rhsc == 'i' || rhsc == 'k');
        } else if (c == 'j') {
            return (rhsc == 'i' || rhsc == 'j');
        } else if (c == 'k') {
            return (rhsc == 'j' || rhsc == 'k');
        }
        return false;
    }

    char c;
    bool negative;
    friend
    std::ostream& operator << (std::ostream& o, const q& q) {
        return o << "q{" << (q.negative ? "-" : "") << q.c << "}";
    }
};

q reduce(const std::vector<q>& qs) {
    assert(!qs.empty());
    q r = qs[0];
    for (size_t i = 1; i != qs.size(); ++i) {
        r = r * qs[i];
    }
    return r;
}

static std::unordered_map<std::string, q> cache;

q reduce(const std::string& input, const size_t start, const size_t last) {
    assert(start <= last);
    const auto l = last - start;
    const size_t min = 64;
    if (l > min) {
        const std::string& s = input.substr(start, last-start);
        auto it = cache.find(s);
        if (it != cache.end()) {
            return it->second;
        }
        q r{input[start]};
        for (size_t i = start+1; i != last; ++i) {
            r *= q{input[i]};
        }
        cache.insert({s,r});
        return r;
    }
    q r{input[start]};
    for (size_t i = start+1; i != last; ++i) {
        r *= q{input[i]};
    }
    return r;
}

bool solutionExists(const int copies, const std::string& base) {
    cache.clear();
    std::string input;
    for (int i = 0; i != copies; ++i) {
        input += base;
    }

    if (input == "ijk") {
        return true;
    }
    if (input.size() <= 3) {
        return false;
    }

    q first = q{input[0]};
    for (int firstEnd = 1; firstEnd < input.size()-2; ++firstEnd) {
        if (firstEnd > 1) {
            first *= q{input[firstEnd-1]};
        }
        if (first == q('i')) {
            std::cerr << "reduce(\"...\", 0, " << firstEnd << ") == " << first << std::endl;

            int secondStart = firstEnd;
            q second{input[secondStart]};
            for (int secondEnd = secondStart+1; secondEnd < input.size()-1; ++secondEnd)
            {
                if (secondEnd != (secondStart+1)) {
                    second *= q{input[secondEnd-1]};
                }
                if (second == q('j')) {
                    q third = reduce(input, secondEnd, input.size());
                    // std::cerr << "secondEnd == " << secondEnd << ", " << second << ", " << third << std::endl;
                    if (third == q('k')) {
                        return true;
                    }
                }
            }
        }
    }

    return false;
}

void testMult(const char* arg) {
    assert(q(arg[0]) == q(arg[1]) * q(arg[2]));
}

void test() {
    testMult("111");
    testMult("i1i");
    testMult("j1j");
    testMult("k1k");

    testMult("ii1");
    assert(q('1',true) == q('i') * q('i'));
    testMult("kij");
    assert(q('j',true) == q('i') * q('k'));

    testMult("jj1");
    assert(q('k',true) == q('j') * q('i'));
    assert(q('1',true) == q('j') * q('j'));
    testMult("ijk");

    testMult("kk1");
    testMult("jki");
    assert(q('i',true) == q('k') * q('j'));
    assert(q('1',true) == q('k') * q('k'));

    assert(q('1',true) == q('1',true) * q('1'));
    assert(q('k') == q('j',true) * q('i'));

    assert(q('i') == reduce({q('j'),q('i'),q('j')}));
    assert(q('j') == reduce({q('i'),q('j'),q('i')}));
    assert(q('k') == reduce({q('j'),q('i'),q('j'),q('i'),q('j'),q('i')}));

    assert(!solutionExists(1, "ik"));
    assert(solutionExists(1, "ijk"));
    assert(!solutionExists(1, "kji"));
    assert(solutionExists(6, "ji"));
    assert(!solutionExists(10000, "i"));
}

int main() {
    test();
    size_t T;
    std::cin >> T;
    for (int i = 0; i != T; ++i) {
        size_t L, X;
        std::cin >> L >> X;
        std::string base;
        std::cin >> base;
        std::cout << "Case #" << (i+1) << ": " << (solutionExists(X, base) ? "YES" : "NO") << std::endl;
    }
}
