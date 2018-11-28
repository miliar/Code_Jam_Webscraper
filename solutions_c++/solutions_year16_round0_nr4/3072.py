#include <fstream>

using namespace std;

int main()
{
    int T, S, C, K, i, j;
    ifstream f("input.in");
    f >> T;
    ofstream g("output.out");
    for (i = 1; i <= T; i++)
    {
        f >> K >> C >> S;
        g << "Case #" << i << ": ";
        for (j = 1; j <= S; j++)
            g << j << ' ';
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}
