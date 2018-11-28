#include <iostream>
#include <string>
#include <vector>

int GetFirst(const std::vector<int> &m)
{
    int total = 0;
    for(int i = 1; i < m.size(); ++i)
    {
        if (m[i] < m[i - 1])
            total += (m[i - 1] - m[i]);
    }
    return total;
}

int GetSecond(const std::vector<int> &m)
{
    int rate;
    bool set = false;
    for(int i = 1; i < m.size(); ++i)
    {
        if (m[i] < m[i - 1])
        {
            int d = m[i - 1] - m[i];
            if (!set || rate < d)
            {
                rate = d;
                set = true;
            }
        }
    }
    int total = 0;
    for(int i = 0; i < m.size() - 1; ++i)
    {
        total += std::min(m[i], rate);
    }
    return total;
}


std::string ReadAndSolve()
{
    int N;
    std::vector<int> v;
    std::cin >> N;

    for(int i = 0; i < N; ++i)
    {
        int q;
        std::cin >> q;
        v.push_back(q);
    }
    return std::to_string(GetFirst(v)) + " " + std::to_string(GetSecond(v));
}

int main()
{
    int t = 0;
    std::cin >> t;

    for(int i = 0; i < t; ++i)
    {
        std::string res = ReadAndSolve();
        std::cout << "Case #" << i + 1 << ": " << res << "\n";
    }
    return 0;
}
