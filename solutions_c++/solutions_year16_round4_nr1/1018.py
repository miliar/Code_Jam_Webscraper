#include <bits/stdc++.h>

typedef std::vector<std::string> vs;
// P R S
template <class C>
int len(const C &c) {
    return (int)c.size();
}

inline std::string comb(const std::string &a, const std::string &b) {
    if (a < b) {
        return a + b;
    } else {
        return b + a;
    }
}

std::string solve(const vs &rock, const vs &paper, const vs &scisors) {
    if (rock.size() + paper.size() + scisors.size() == 1) {
        for (const vs &x : {rock, paper, scisors}) {
            if (!x.empty())
                return x[0];
        }
        assert(false);
    }
    int r_p = (len(paper) + len(rock) - len(scisors)) / 2;
    bool cond = (len(paper) + len(rock) - len(scisors)) % 2 == 0;
    int r_s = len(rock) - r_p;
    int s_p = len(paper) - r_p;
    cond = cond && r_p <= len(rock) && r_p <= len(paper);
    cond = cond && r_s <= len(rock) && r_s <= len(scisors);
    cond = cond && s_p <= len(scisors) && s_p <= len(paper);
    cond = cond && r_p + r_s == len(rock) && r_p + s_p == len(paper)
        && r_s + s_p == len(scisors);
    cond = cond && s_p == len(scisors) - r_s;
    if (!cond)
        return "IMPOSSIBLE";
    vs nr, np, ns;
    int rp = 0, pp = 0, sp = 0;
    for (int i = 0; i < r_p; ++i) {
        np.push_back(comb(paper[pp++], rock[rp++]));
    }
    for (int i = 0; i < s_p; ++i) {
        ns.push_back(comb(paper[pp++], scisors[sp++]));
    }
    for (int i = 0; i < r_s; ++i) {
        nr.push_back(comb(rock[rp++], scisors[sp++]));
    }
    return solve(nr, np, ns);
}
    
int main() {
    FILE *in = fopen("input.txt", "r");
    FILE *out = fopen("output.txt", "w");
    int t;
    fscanf(in, "%d", &t);
    for (int test_number = 1; test_number <= t; ++test_number) {
        int n, r, p, s;
        fscanf(in, "%d%d%d%d", &n, &r, &p, &s);
        std::vector<std::string> rocks(r, "R");
        std::vector<std::string> papers(p, "P");
        std::vector<std::string> scisors(s, "S");
        fprintf(out, "Case #%d: %s\n", test_number,
                solve(rocks, papers, scisors).c_str());
    }
    fclose(out);
    fclose(in);
}
