#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        unsigned short N = 0;
        cin >> N;
        vector<unsigned int> P;
        for (unsigned int n = 0; n < N; ++n)
        {
            unsigned int p = 0;
            cin >> p;
            P.push_back(p);
        }

        string ps("");
        unsigned int sum = accumulate(P.begin(), P.end(), 0);
        while (sum)
        {
            auto mx = max_element(P.begin(), P.end());
            ps.append(1, static_cast<char>('A' + distance(P.begin(), mx)));
            --(*mx); --sum;
            if (!sum)
                break;

            mx = max_element(P.begin(), P.end());
            --(*mx); --sum;
            auto nx = max_element(P.begin(), P.end());
            if ((*nx)*2 > sum)
            {
                ++(*mx); ++sum;
            }
            else
                ps.append(1, static_cast<char>('A' + distance(P.begin(), mx)));

            if (sum)
                ps.append(1, ' ');
        }
        cout << "Case #" << t << ": " << ps << '\n';
    }
}
