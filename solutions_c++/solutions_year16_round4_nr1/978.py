// vim:set sw=4 et smarttab:
// Round 2 2016

#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>

int n, r, p, s;
const int rock = 0, paper = 1, scissors = 2;

void require(int n, int rps, int &r, int &p, int &s)
{
    static bool memo[13][3];
    static int memo_r[13][3];
    static int memo_p[13][3];
    static int memo_s[13][3];

    if (memo[n][rps])
    {
        r = memo_r[n][rps];
        p = memo_p[n][rps];
        s = memo_s[n][rps];
        return;
    }
    r = p = s = 0;
    if (n == 0)
    {
        if (rps == rock)
            r = 1;
        else if (rps == paper)
            p = 1;
        else if (rps == scissors)
            s = 1;
        else
            assert(false);
    }
    else
    {
        int tr, tp, ts;
        require(n - 1, rps, tr, tp, ts);
        r += tr, p += tp, s += ts;
        require(n - 1, (rps + 2) % 3, tr, tp, ts);
        r += tr, p += tp, s += ts;
    }
    memo[n][rps] = true;
    memo_r[n][rps] = r;
    memo_p[n][rps] = p;
    memo_s[n][rps] = s;
}

std::string make(int n, int rps)
{
    static std::string memo[13][3];
    if (!memo[n][rps].empty())
        return memo[n][rps];
    std::string ret;
    if (n == 0)
    {
        if (rps == rock)
            ret = "R";
        else if (rps == paper)
            ret = "P";
        else if (rps == scissors)
            ret = "S";
        else
            assert(false);
    }
    else
    {
        std::string a, b;
        a = make(n - 1, rps);
        b = make(n - 1, (rps + 2) % 3);
        if (a < b)
            ret = a + b;
        else
            ret = b + a;
    }
    memo[n][rps] = ret;
    return ret;
}

std::string solve()
{
    std::vector<std::string> candidate;
    int rr, rp, rs;
    require(n, rock, rr, rp, rs);
    if (rr == r && rp == p && rs == s)
        candidate.push_back(make(n, rock));
    require(n, paper, rr, rp, rs);
    if (rr == r && rp == p && rs == s)
        candidate.push_back(make(n, paper));
    require(n, scissors, rr, rp, rs);
    if (rr == r && rp == p && rs == s)
        candidate.push_back(make(n, scissors));
    if (candidate.empty())
        return "IMPOSSIBLE";
    return *min_element(candidate.begin(), candidate.end());
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        std::string answer = solve();
        printf("Case #%d: %s\n", tc, answer.c_str());
    }
}
