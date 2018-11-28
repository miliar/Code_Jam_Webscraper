#include <fstream>
#include <iostream>
using namespace std;

bool solve (int X, int R, int C)
{
    int cellCount = R * C;

    if (X == 1)
        return true;
    if (X == 2)
        return (cellCount % 2 == 0);
    if (X == 3)
        return (cellCount == 6 || cellCount == 9 || cellCount == 12);
    if (X == 4)
        return (cellCount == 12 || cellCount == 16);

    return false;    // Incorrect value for X, R, C > 4
}

int main()
{
    freopen("D-input.txt", "r", stdin);
    freopen("D-output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; testCase++)
    {
        int X, R, C;
        cin >> X >> R >> C;

        bool gabrielWins = solve (X, R, C);
        cout << "Case #" << testCase << ": ";
        cout << (gabrielWins ? "GABRIEL" : "RICHARD") << endl;
    }
    
    return 0;
}
