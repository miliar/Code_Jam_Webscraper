#include <bits/stdc++.h>
#define long long long
#define MOD ((int)1e9 + 7)


bool check_string(const std::string & s)
{
    std::vector <char> u(128, 0);
    char c = s[0];
    u[c] = 1;
    for (int i = 1; i < (int)s.size(); ++i)
    {
        c = s[i];
        if (c != s[i-1] && u[c])
            return false;
        u[c] = 1;
    }
    return true;
}


std::string new_string(const std::string & s)
{
    std::string r(1, s[0]);
    for (int i = 1; i < (int)s.size(); ++i)
        if (s[i] != r[r.size()-1])r += s[i];
    return r;
}


long brute(const std::vector <std::string> & v)
{
    std::cerr << "Brute\n";
    long count = 0ll;
    std::vector <int> perm;
    for (int i = 0; i < (int)v.size(); ++i)
    {
        perm.push_back(i);
    }
    do
    {
        bool ok = true;
        std::vector <char> u(128, 0);
        for (int i = 0; ok && i < (int)perm.size(); ++i)
        {
            int j = perm[i];
            for (int k = 0; ok && k < (int)v[j].size(); ++k)
            {
                char c = v[j][k];
                if (k == 0)
                {
                    if (i)
                    {
                        int p = perm[i-1];
                        int pp = v[p].size()-1;
                        if (u[c] && v[p][pp] != c)
                        {
                            ok = false;
                        }
                    }
                }
                else
                {
                    if (v[j][k-1] != c && u[c])
                    {
                        ok = false;
                    }
                }
                u[c] = 1;
            }
        }
        if (ok)
        {
            ++count;
            if (count >= MOD) count -= MOD;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    return count;
}


void solve(std::istream & in, std::ostream & out)
{
    int T;
    in >> T;
    for (int t = 1; t <= T; ++t)
    {
        out << "Case #" << t << ": ";
        bool ok = true;
        int n;
        in >> n;
        std::vector <std::string> v(n);
        for (int i = 0; i < n; ++i)
        {
            in >> v[i];
            v[i] = new_string(v[i]);
            ok = ok && check_string(v[i]);
        }
        if (!ok)
        {
            out << 0 << std::endl;
        }
        else
        {
            out << brute(v) << std::endl;
        }
    }
}


int main()
{
    std::ifstream in("B-small-attempt1.in");
    std::ofstream out("b1.out");

    solve(in, out);

    out.close();
    in.close();
}
