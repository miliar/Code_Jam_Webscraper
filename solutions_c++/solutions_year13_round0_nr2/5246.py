
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fou("out");

    int t;
    fin >> t;
    int lawn[100][100];

    for (int i = 0; i < t; ++i) {
        int n, m;
        fin >> n >> m;

        fou << "Case #" << i + 1 << ": ";

        for (int r = 0; r < n; ++r)
            for (int c = 0; c < m; ++c)
                fin >> lawn[r][c];

        if (1 == n || 1 == m) {
            fou << "YES" << endl;
            continue;
        }

        bool flag = false;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {

                bool die[4] = {false};
                for (int k = r - 1; k >= 0; --k)
                    if (lawn[k][c] > lawn[r][c]) { die[0] = true; break; }
                for (int k = c + 1; k < m; ++k)
                    if (lawn[r][k] > lawn[r][c]) { die[1] = true; break; }

                if (die[0] && die[1]) { flag = true; break; }

                for (int k = r + 1; k < n; ++k)
                    if (lawn[k][c] > lawn[r][c]) { die[2] = true; break; }

                if (die[1] && die[2]) { flag = true; break; }

                for (int k = c - 1; k >= 0; --k)
                    if (lawn[r][k] > lawn[r][c]) { die[3] = true; break; }

                if ((die[3] && die[0]) ||
                    (die[3] && die[2])) { flag = true; break; }
            }
            if (flag) break;

        }

        if (flag) fou << "NO" << endl;
        else fou << "YES" << endl;
    }
    return 0;
}
