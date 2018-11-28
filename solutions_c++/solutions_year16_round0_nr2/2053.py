#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int ans(string s)
{
    int ctr = 0;

    while (true)
    {
        while (s.back() == '+')
            s.pop_back();

        if (s.empty())
            return ctr;

        else if (s.front() == '-')
        {
            reverse(s.begin(), s.end());

            for (string::iterator i = s.begin(); i != s.end(); ++i)
            {
                if (*i == '+')
                    *i = '-';

                else
                    *i = '+';
            }

            ++ctr;
        }

        else
        {
            string::iterator i, j;

            for (i = s.end() - 1; i != s.begin(); --i)
            {
                if (*i == '+')
                    break;

                //*i = '-';
            }

            reverse(s.begin(), i + 1);

            for (j = s.begin(); j != i + 1; ++j)
            {
                if (*j == '+')
                    *j = '-';

                else
                    *j = '+';
            }


            ++ctr;
        }

    }
}

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t;
    string s;

    in >> t;

    for (int i = 1; i <= t; ++i)
    {
        in >> s;
        out << "Case #" << i << ": " << ans(s) << '\n';
    }
}
