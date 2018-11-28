#include <bits/stdc++.h>

using namespace std;

int T , j , nr , i;
string s;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");

    fin >> T;
    for (i = 1; i <= T; ++i)
    {
        fin >> s;

        j = 0; nr = 0;
        while (true)
        {
            while (j + 1 < s.size() && s[j+1] == s[j])
                j++;

            nr++;

            if (j == s.size() - 1) break;

            j++;
        }

        if (s.back() == '+') nr--;

        fout << "Case #" << i << ": " << nr << '\n';
    }

    return 0;
}
