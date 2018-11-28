#include <vpc/vpc.h>

using namespace vp;

#define dp(...)

// -------------------------------------------------------------------------------------------------

typedef std::map<std::pair<int, int>, int> DP;

bool iscons(char ch) {
    return !any_of_val(ch, 'a', 'e', 'i', 'o', 'u');
} 

int solve_rec(DP& dynp, const std::string& w, const int pos, const int nn)
{
    if (pos == (int)w.size()) return 0;
    if (nn == 0) {
        return w.size() - pos;
    }

    dp("XX", w.substr(pos), pos, nn);

    vpassert(pos < (int)w.size());
    bool isvow = any_of_val(w[pos], 'a', 'e', 'i', 'o', 'u');

    auto mpair = std::make_pair(pos, nn);
    auto p = dynp.find(mpair);
    if (p != dynp.end()) return p->second;

    vpassert(nn > 0);

    int cnt=0;
    if (isvow) {
        cnt = solve_rec(dynp, w, pos+1, nn);
    }
    else {
        cnt = solve_rec(dynp, w, pos+1, nn);
        int i = pos;
        int nc = nn;
        while (i < (int)w.size()) {
            if (!iscons(w[i])) break;
            nc--;
            if (nc == 0) {
                cnt = w.size() - i;
#if 0
                if (i+1 == (int)w.size() || iscons(w[i+1]))
                {
                    cnt += 1;
                }
                else {
                }
                break;
#endif
            }
            i++;
        }
    }

    dynp[mpair] = cnt;
    dp("RET", w.substr(pos), pos, nn, cnt);
    return cnt;
}

int solve(const std::string& w, int n)
{
    DP dynp;

    int cnt=0;
    int i= 0;
    while (i < (int)w.size()) {
        cnt += solve_rec(dynp, w, i, n);
        i++;
    }
    return cnt;
}

// -------------------------------------------------------------------------------------------------

int main(int argc, char** argv)
{
    vpassert(argc>1);
    std::ifstream f;
    std::ofstream fout;

    openr(f, argv[1]);
    openw(fout, "out.txt");

    int n;
    readln_vars(f, n);

    for (int i: nrange(0, n)) {
        std::string w;
        int n;
        auto l = readln_parts(f);
        vpassert(l.size() == 2);
        w = l[0];
        n = std::stoi(l[1]);
        vpassert(n > 0);

        fout << "Case #" << i+1 << ": " << solve(w, n)  << "\n";
    }
}
