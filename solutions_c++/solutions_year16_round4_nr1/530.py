#include <cassert>
#include <cstdio>
#include <tuple>
#include <string>
#include <vector>

typedef std::tuple<int, int, int> Tuple;

const std::string IMPOSSIBLE = "IMPOSSIBLE";

std::string concat(std::string a, std::string b)
{
    return std::min(a + b, b + a);
}

std::string solve(int n, int a, int b, int c)
{
    std::string sa = "P", sb = "R", sc = "S";
    for (int i = 0; i < n; ++ i) {
        int A = (a + b - c) / 2;
        int B = (b + c - a) / 2;
        int C = (c + a - b) / 2;
        if (A < 0 || B < 0 || C < 0) {
            return IMPOSSIBLE;
        }
        std::tie(a, b, c) = std::tie(A, B, C);
        std::string SA = concat(sa, sb);
        std::string SB = concat(sb, sc);
        std::string SC = concat(sc, sa);
        std::tie(sa, sb, sc) = std::tie(SA, SB, SC);
    }
    assert(a + b + c == 1);
    if (a) {
        return sa;
    }
    if (b) {
        return sb;
    }
    return sc;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        int n, b, a, c;
        scanf("%d%d%d%d", &n, &b, &a, &c);
        printf("Case #%d: %s\n", t, solve(n, a, b, c).c_str());
    }
}
