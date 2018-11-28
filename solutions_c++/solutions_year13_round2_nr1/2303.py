#include <iostream>
#include <vector>
#include <algorithm>

size_t best = 0;

unsigned moves(unsigned smote, std::vector<unsigned> const &motes, size_t current = 0) {

    if (current >= best)
        return best;

    std::vector<unsigned> cmotes(motes);
    while (!cmotes.empty() && smote > cmotes[0]) {
        smote += cmotes[0];
        cmotes.erase(cmotes.begin());
    }

    if (cmotes.empty())
        return best = current;

    // no possible move. either
    // (a) add the largest possible mote (smote - 1) to smote or
    // (b) remove one of the current motes (expensive)

    unsigned res = ~0U;

    // a
    if (smote > 1)
        res = moves(smote + (smote - 1), cmotes, current + 1);

    // b
    for (size_t idx = 0; idx < cmotes.size(); ++idx) {
        unsigned val = cmotes[idx];
        cmotes.erase(cmotes.begin() + idx);
        unsigned r = moves(smote, cmotes, current + 1);
        cmotes.insert(cmotes.begin() + idx, val);
        if (r < res)
            res = r + 1;
    }

    if (res >= best)
        res = best;

    return res;

    //return motes.size() < p1 ? motes.size() : p1;
}

unsigned max_moves(unsigned smote, std::vector<unsigned> const &motes) {

//    std::cout << ":" << smote << "/" << motes.size() << "." << motes[0] << '\n';

    std::vector<unsigned> cmotes(motes);
    while (!cmotes.empty() && smote > cmotes[0]) {
        smote += cmotes[0];
        cmotes.erase(cmotes.begin());
    }

    if (cmotes.empty())
        return 0;

    // no possible move. either
    // (a) add the largest possible mote (smote - 1) to smote or
    // (b) remove one of the current motes (expensive)

    unsigned res = ~0U;

    // a
    if (smote > 1)
        res = max_moves(smote + (smote - 1), cmotes) + 1;

    return motes.size() < res ? motes.size() : res;
}

int main() {

    size_t T;
    std::cin >> T;

    for (size_t test = 0; test < T; ++test) {
        unsigned smote, nmotes;
        std::cin >> smote >> nmotes;

        std::vector<unsigned> motes;
        //motes.resize(nmotes);
        for (size_t idx = 0; idx < nmotes; ++idx) {
            size_t x;
            std::cin >> x;
            motes.push_back(x);
            //std::cin >> motes[idx];
        }
        std::sort(motes.begin(), motes.end());
        best = max_moves(smote, motes);
        std::cout << "Case #" << test + 1 << ": " << moves(smote, motes) << '\n';
    }
}
