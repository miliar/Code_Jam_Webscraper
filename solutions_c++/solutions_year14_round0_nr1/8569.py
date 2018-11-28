#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("output");

    int t;
    int a[5][5], b[5][5];
    infile >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        int ans = 0;
        int x;
        infile >> x;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                infile >> a[i][j];
        int y;
        infile >> y;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                infile >> b[i][j];

        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
                if (a[x][i] == b[y][j])
                {
                    if (ans != 0)
                    {
                        ans = -1;
                        break;
                    }
                    ans = a[x][i];
                }
            if (ans == -1) break;
        }

        outfile << "Case #" << ca << ": ";
        if (ans == 0) outfile << "Volunteer cheated!" << endl;
        else if (ans == -1) outfile << "Bad magician!" << endl;
        else outfile << ans << endl;
    }
    return 0;
}
