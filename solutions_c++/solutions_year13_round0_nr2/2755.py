#include <iostream>
#include <fstream>
#include <vector>
#include <array>

int main()
{
    std::ifstream in("B-small-attempt1.in");
    std::ofstream out("test.out");
    int t;
    in >> t;
    for (int q = 1; q <= t; ++q)
    {
        out << "Case #" << q << ": ";
        std::vector<std::vector<int>> a;
        int n, m;
        in >> n >> m;
        a.resize(n);
        for (size_t i = 0; i < a.size(); ++i)
        {
            a[i].resize(m);
            for (size_t j = 0; j < a[i].size(); ++j)
            {
                in >> a[i][j];
            }
        }
        std::vector<std::vector<int>> v(n);
        for (size_t i = 0; i < v.size(); ++i)
        {
            v[i].resize(m);
        }
        n = (1 << n);
        m = (1 << m);
        bool f = false;
        for (int i = 0; i < n; ++i)
        {
            if (f)
            {
                break;
            }
            for (int j = 0; j < m; ++j)
            {
                for (int k = 0; k < v.size(); ++k)
                {
                    for (int l = 0; l < v[k].size(); ++l)
                    {
                        if (i & (1 << k))
                        {
                            v[k][l] = 2;
                        }
                        else
                        {
                            v[k][l] = 1;
                        }
                    }
                }
                bool local_f = true;
                for (int k = 0; k < v.size(); ++k)
                {
                    for (int l = 0; l < v[k].size(); ++l)
                    {
                        if (!(j & (1 << l)))
                        {
                            v[k][l] = 1;
                        }
                        if (v[k][l] != a[k][l])
                        {
                            local_f = false;
                            continue;
                        }
                    }
                }
                if (local_f)
                {
                    f = true;
                    break;
                }
            }
        }
        if (f)
        {
            out << "YES" << std::endl;
        }
        else
        {
            out << "NO" << std::endl;
        }
    }
    return 0;
}

