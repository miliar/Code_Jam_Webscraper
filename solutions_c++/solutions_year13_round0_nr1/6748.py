#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;

ifstream cin("in");
ofstream cout("out");

char t[4][4];
int v[4][3], h[4][3], d1[3], d2[3];

void clear()
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 3; j++)
            v[i][j] = h[i][j] = d1[j] = d2[j] = 0;
}

int tr(char c)
{
    switch (c) {
        case 'X': return 0;
        case 'O': return 1;
        case 'T': return 2;
    }
    return 0;
}

void solve(int cs)
{
    int g = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
            cin >> t[i][j];
            if (t[i][j] != '.') {
                g++;
                int z = tr(t[i][j]);
                h[i][z]++;
                v[j][z]++;
                if (i == j)
                    d1[z]++;
                if (i + j == 3)
                    d2[z]++;
            }
        }
    int w = 2;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 2; j++) {
            if (h[i][j] == 4 || (h[i][j] == 3 && h[i][2] == 1))
                w = j;
            if (v[i][j] == 4 || (v[i][j] == 3 && v[i][2] == 1))
                w = j;
            if (d1[j] == 4 || (d1[j] == 3 && d1[2] == 1))
                w = j;
            if (d2[j] == 4 || (d2[j] == 3 && d2[2] == 1))
                w = j;
        }
    }
    cout << "Case #" <<cs << ": ";
    switch (w) {
        case 0:
            cout << "X won";
            break;
        case 1:
            cout << "O won";
            break;
        case 2:
            if (g == 16)
                cout << "Draw";
            else
                cout << "Game has not completed";
            break;
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        clear();
        solve(i + 1);
    }
    return 0;
}
