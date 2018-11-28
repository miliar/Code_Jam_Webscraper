#include <fstream>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t, sMax, ctr, ans;
    char s[1005];

    in >> t;

    for (int j = 1; j <= t; ++j)
    {
        ctr = ans = 0;

        in >> sMax >> s;

        for (int i = 0; i < sMax + 1; ++i)
        {
            if (ctr < i)
            {
                ans += i - ctr;
                ctr = i;
            }

            ctr += s[i] - '0';
        }

        out << "Case #" << j << ": " << ans << '\n';
    }

    return 0;
}
