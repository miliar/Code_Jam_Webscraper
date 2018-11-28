#include <fstream>

using namespace std;

int main()
{
    int tests;
    int k, c, s;
    int i;
    ifstream f("fractiles.in");
    ofstream g("fractiles.out");
    f >> tests;
    for (int l = 1; l <= tests; l++)
    {
        f >> k >> c >> s;
        g << "Case #" << l << ": ";
        if (s < k)
            g << "IMPOSSIBLE";
        else
        {
            for (i = 1; i <= k; i++)
                g << i << " ";
        }
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}
