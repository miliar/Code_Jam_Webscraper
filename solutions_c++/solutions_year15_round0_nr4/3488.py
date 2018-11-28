#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;


ifstream fin;
ofstream fout;


int solve(int X, int R, int C)
{
    if (X == 1) return 0;
    if (X == 2) return (R%2) * (C%2);
    if (X == 4 && R*C == 8) return 1;
    if (X >= 7) return 1;
    if ((R*C) % X != 0) return 1;
    if (R < X && C < X) return 1;
    int minrc = (R < C) ? R : C;
    if (X >= 2 * minrc + 1) return 1;

    return 0;
}


int main()
{
    fin.open("in.txt");
    fout.open("out.txt");

    int cases, ci;
    int ans;
    int X, R, C;
    fin >> cases;
    for (ci=1; ci<=cases; ci++)
    {
        cout << "Case " << ci << "...";
        fin >> X >> R >> C;
        ans = solve(X, R, C);
        if (ans)
            fout << "Case #" << ci << ": RICHARD" << endl;
        else
            fout << "Case #" << ci << ": GABRIEL" << endl;
        cout << "ok." << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
