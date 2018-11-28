#include <fstream>
#include <algorithm>

using namespace std;

string ans[5][5][5];

int main()
{
    ifstream cin("easy.in");
    ofstream cout("easy.out");

    //O linie
    ans[1][1][1] = '0';
    ans[1][1][2] = '1';
    ans[1][1][3] = '1';
    ans[1][1][4] = '1';

    ans[1][2][1] = '0';
    ans[1][2][2] = '0';
    ans[1][2][3] = '1';
    ans[1][2][4] = '1';

    ans[1][3][1] = '0';
    ans[1][3][2] = '1';
    ans[1][3][3] = '1';
    ans[1][3][4] = '1';

    ans[1][4][1] = '0';
    ans[1][4][2] = '0';
    ans[1][4][3] = '1';
    ans[1][4][4] = '1';

    //2 linii
    ans[2][2][1] = '0';
    ans[2][2][2] = '0';
    ans[2][2][3] = '1';
    ans[2][2][4] = '1';

    ans[2][3][1] = '0';
    ans[2][3][2] = '0';
    ans[2][3][3] = '0';
    ans[2][3][4] = '1';

    ans[2][4][1] = '0';
    ans[2][4][2] = '0';
    ans[2][4][3] = '1';
    ans[2][4][4] = '1';

    //3 linii
    ans[3][3][1] = '0';
    ans[3][3][2] = '1';
    ans[3][3][3] = '0';
    ans[3][3][4] = '1';

    ans[3][4][1] = '0';
    ans[3][4][2] = '0';
    ans[3][4][3] = '0';
    ans[3][4][4] = '0';

    //4 linii
    ans[4][4][1] = '0';
    ans[4][4][2] = '0';
    ans[4][4][3] = '1';
    ans[4][4][4] = '0';

    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
                for (int k = 1; k <= 4; k++)
                    if (ans[i][j][k] == "0")
                        ans[i][j][k] = "GABRIEL";
                    else if (ans[i][j][k] == "1")
                        ans[i][j][k] = "RICHARD";

    int t = 64;
    cin >> t;

    int x, r, c;
    for (int i = 1; i <= t; i++) {
        cin >> x >> r >> c;

        if (c < r)
            swap(r, c);
        cout << "Case #" << i << ": " << ans[r][c][x] << '\n';
    }

    cin.close();
    cout.close();
    return 0;
}
