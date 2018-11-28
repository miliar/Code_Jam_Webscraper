#include <bits/stdc++.h>

using namespace std;

string S;
int Smax, T;

int main()
{
    ifstream in("large.in");
    ofstream out("data.out");

    in >> T;

    for (int t = 1; t <= T; ++t)
    {
        in >> Smax >> S;

        int standing = 0;
        int sol = 0;

        for (int i = 0; i <= Smax; ++i)
        {
            int d = S[i] - '0';

            if (d)
            {
                int dif = max(0, i - standing);

                sol += dif;
                standing += dif + d;
            }
        }

        out << "Case #" << t << ": " << sol << "\n";
    }

    return 0;
}
