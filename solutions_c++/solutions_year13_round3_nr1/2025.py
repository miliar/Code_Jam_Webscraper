#include <iostream>
#include <vector>
#include <string>

inline bool is_cons(char x) {
    return x != 'a' && x != 'e' && x != 'i' && x != 'o' && x != 'u';
}

unsigned long long asum(unsigned n) {
    unsigned long long out = 0;
    for (size_t x = 1; x < n; ++x)
        out += x;
    return out;
}

unsigned long long n_score(std::string const &name, unsigned n) {

    // find all indices at which [n] consonants can be read.
    unsigned long long score = 0;
    size_t const L = name.length();
    std::vector<bool> startpoint(L, false);
    for (size_t idx = 0; idx <= L - n; ++idx) {
        bool ok = true;
        for (size_t tpos = 0; ok && tpos < n; ++tpos)
            ok = is_cons(name[idx + tpos]);
        if (!ok)
            continue;

        startpoint[idx] = true;
        unsigned nstart_idx = ((L + 1) - n) - idx;
        score += nstart_idx;
        size_t cidx = idx;
        while (cidx--) {
            if (!startpoint[cidx]) {
                startpoint[cidx] = true;
                score += nstart_idx;
            }
        }
    }

    return score;

}

int main() {

    size_t T;
    std::cin >> T;

    for (size_t test = 0; test < T; ++test) {

        std::string name;
        unsigned n;
        std::cin >> name >> n;


        std::cout << "Case #" << test + 1 << ": " << n_score(name, n) << '\n';
    }
}
