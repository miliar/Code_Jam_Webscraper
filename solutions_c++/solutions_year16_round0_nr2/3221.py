#include <fstream>
#include <cstring>

using namespace std;
char s[101];

int compute()
{
    int flips = 0;
    int l = strlen(s);
    while (s[l - 1] == '+' && l > 0)
        l--;
    for (int i = 1; i < l; i++)
    {
        if (s[i] != s[i - 1])
        {
            flips++;
        }
    }
    if (l > 0)
    {
        if (s[l - 1] == '-')
            flips++;
    }
    return flips;
}

int main()
{
    int tests;
    ifstream f("pancakes.in");
    ofstream g("pancakes.out");
    f >> tests;
    for (int k = 1; k <= tests; k++)
    {
        f >> s;
        g << "Case #" << k << ": " << compute() << '\n';
    }
    f.close();
    g.close();
    return 0;
}
