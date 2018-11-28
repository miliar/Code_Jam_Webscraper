#include <bits/stdc++.h>


std::ifstream in("input.txt");
std::ofstream out("output.txt");

const std::string BAD = "Bad magician!";
const std::string CHEAT = "Volunteer cheated!";


int main()
{
    int C;
    in >> C;
    for (int t = 1; t <= C; ++t)
    {
        out << "Case #" << t << ": ";
        int r, k = 0, last = 1;
        std::set < int > s;
        in >> r;
        for (int i = 1; i < 5; ++i)
        {
            for (int j = 1; j < 5; ++j)
            {
                int x;
                in >> x;
                if (i == r)
                {
                    s.insert(x);
                }
            }
        }
        in >> r;
        for (int i = 1; i < 5; ++i)
        {
            for (int j = 1; j < 5; ++j)
            {
                int x;
                in >> x;
                if (i == r)
                {
                    if (s.find(x) != s.end())
                    {
                        ++k;
                        last = x;
                    }
                }
            }
        }
        if (k == 1)
        {
            out << last << std::endl;
        }
        else if (k > 1)
        {
            out << BAD << std::endl;
        }
        else
        {
            out << CHEAT << std::endl;
        }
    }
    in.close();
    out.close();
}
