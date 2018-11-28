#include <fstream>

using namespace std;

ifstream cin ("A-small-attempt3.in");
ofstream cout ("b.txt");

string A[4][4];
int n, i, j, k, x, y;
string s;
bool b = 0;

int main()
{
    cin >> n;
    for (i = 1; i <= n; ++i)
    {
        b = 0;
        for (j = 0; j < 4; ++j)
        {
            cin >> s;
            for (k = 0; k < 4; ++k)
            {
                A[j][k] = s.substr(k, 1);
                if (A[j][k] == "T")
                {
                    x = j;
                    y = k;
                }
                if (A[j][k] == ".")
                    b = 1;
            }
        }
        A[x][y] = "X";
        if (A[0][0] + A[0][1] + A[0][2] + A[0][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[1][0] + A[1][1] + A[1][2] + A[1][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[2][0] + A[2][1] + A[2][2] + A[2][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[3][0] + A[3][1] + A[3][2] + A[3][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][0] + A[1][0] + A[2][0] + A[3][0] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][1] + A[1][1] + A[2][1] + A[3][1] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][2] + A[1][2] + A[2][2] + A[3][2] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][3] + A[1][3] + A[2][3] + A[3][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][0] + A[1][1] + A[2][2] + A[3][3] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else if (A[0][3] + A[1][2] + A[2][1] + A[3][0] == "XXXX")
            cout << "Case #" << i << ": X won" << endl;
        else
        {
        A[x][y] = "O";
        if (A[0][0] + A[0][1] + A[0][2] + A[0][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[1][0] + A[1][1] + A[1][2] + A[1][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[2][0] + A[2][1] + A[2][2] + A[2][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[3][0] + A[3][1] + A[3][2] + A[3][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][0] + A[1][0] + A[2][0] + A[3][0] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][1] + A[1][1] + A[2][1] + A[3][1] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][2] + A[1][2] + A[2][2] + A[3][2] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][3] + A[1][3] + A[2][3] + A[3][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][0] + A[1][1] + A[2][2] + A[3][3] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (A[0][3] + A[1][2] + A[2][1] + A[3][0] == "OOOO")
            cout << "Case #" << i << ": O won" << endl;
        else if (b)
            cout <<  "Case #" << i << ": Game has not completed" << endl;
        else
            cout <<  "Case #" << i << ": Draw" << endl;
        }
    }
}
