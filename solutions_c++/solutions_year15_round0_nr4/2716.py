#include <fstream>


using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t, x, r, c, flag;

    in >> t;

    for (int j = 1; j <= t; ++j)
    {
        in >> x >> r >> c;

        flag = 0;

        if (r * c < x)
            flag = 1;

        else if (r * c % x != 0)
            flag = 1;

        else if (x > max(r, c))
            flag = 1;

        else if (x >= 7)
            flag = 1;

        else if (x > 2 * min(r,c))
            flag = 1;

        else if (x == 4 and r + c == 6 and r * c == 8)
            flag = 1;

        out << "Case #" << j << ": ";

        if (flag)
            out << "RICHARD\n";

        else
            out << "GABRIEL\n";
    }

    return 0;
}
