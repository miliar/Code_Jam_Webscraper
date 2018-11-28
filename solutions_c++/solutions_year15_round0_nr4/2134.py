#include <fstream>

using namespace std;

int main()
{
    int T, i, j, X, R, C;
    ifstream f("input.in");
    f >> T;

    ofstream g("output.out");
    for (i = 1; i <= T; i++)
    {
        f >> X >> R >> C;
        g << "Case #" << i << ": ";
        if (X >= 7)
            g << "RICHARD";
        else if (X > R && X > C)
            g << "RICHARD";
        else if (R * C % X != 0)
            g << "RICHARD";
        else if ((X + 1) / 2 > R || (X + 1) / 2 > C)
            g << "RICHARD";
        else if (X == 1 || X == 2 || X == 3)
            g << "GABRIEL";
        else if (X == 4)
        {
            if (min(R, C) > 2)
                g << "GABRIEL";
            else
                g << "RICHARD";
        }
        else if (X == 5)
        {
            if (!(min(R, C) == 3 && max(R, C) == 5))
                g << "GABRIEL";
            else
                g << "RICHARD";
        }
        else if (X == 6)
        {
            if (min(R, C) > 3)
                g << "GABRIEL";
            else
                g << "RICHARD";
        }
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}
