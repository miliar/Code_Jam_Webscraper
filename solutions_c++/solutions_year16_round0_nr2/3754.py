#include <fstream>

using namespace std;

int main()
{
    int T, i, j, k;
    char active;
    string s;
    ifstream f("input.in");
    ofstream g("output.out");
    f >> T;
    for (i = 1; i <= T; i++)
    {
        f >> s;
        k = 0;
        active = s[0];
        for (j = 1; j < s.size(); j++)
            if (s[j] != active)
            {
                k++;
                active = s[j];
            }

        if (active == '-')
            k++;
        g << "Case #" << i << ": " << k << '\n';
    }

    f.close();
    g.close();
    return 0;
}
