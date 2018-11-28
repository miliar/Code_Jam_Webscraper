#include <bits/stdc++.h>


int test_case(int n, const std::string& s)
{
    int ans = 0;
    int total = s[0] - '0';
    for (int i = 1; i < (int)s.size(); ++i)
    {
        int k = s[i] - '0';
        if (k > 0 && i > total)
        {
            int d = i - total;
            ans += d;
            total += d;
        }
        total += k;
    }
    return ans;
}


void solve(std::istream& in, std::ostream& out)
{
    int T;
    in >> T;
    for (int test = 1; test <= T; ++test)
    {
        int n;
        std::string s;
        in >> n >> s;
        int ans = test_case(n, s);
        out << "Case #" << test << ": " << ans << "\n";
    }
}


int main()
{
    std::ifstream ifs("A-large.txt");
    std::ofstream ofs("out_a.txt");
    solve(ifs, ofs);
    ofs.close();
    ifs.close();
}
