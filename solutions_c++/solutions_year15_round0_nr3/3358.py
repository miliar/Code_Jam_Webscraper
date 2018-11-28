#include <iostream>
#include <string>

using namespace std;

int mulMatrix[5][5];

void initMulMatrix();
int mul(int a, int b);
int convert(char c);

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    initMulMatrix();
    for(int t = 1; t <= T; t++)
    {
        int L, X;
        string singleLine, composedLine;
        cin >> L >> X;
        cin >> singleLine;
        for(int i = 0; i < X; i++)
            composedLine += singleLine;
        int result = 1;
        bool gotI = false, gotJ = false;
        for(int i = 0; i < composedLine.size(); i++)
        {
            result = mul(result, convert(composedLine[i]));
            if(result == 2 && !gotI)
            {
                gotI = true;
                result = 1;
            }
            if(result == 3 && gotI && !gotJ)
            {
                gotJ = true;
                result = 1;
            }
        }
        bool ijk = (result == 4 ) && gotI && gotJ;
        cout << "Case #" << t << ": " << (ijk ? "YES" : "NO") << endl;
    }
    return 0;
}

void initMulMatrix()
{
    mulMatrix[1][1] = 1;
    mulMatrix[1][2] = 2;
    mulMatrix[1][3] = 3;
    mulMatrix[1][4] = 4;

    mulMatrix[2][1] = 2;
    mulMatrix[2][2] = -1;
    mulMatrix[2][3] = 4;
    mulMatrix[2][4] = -3;

    mulMatrix[3][1] = 3;
    mulMatrix[3][2] = -4;
    mulMatrix[3][3] = -1;
    mulMatrix[3][4] = 2;

    mulMatrix[4][1] = 4;
    mulMatrix[4][2] = 3;
    mulMatrix[4][3] = -2;
    mulMatrix[4][4] = -1;
}

int mul(int a, int b)
{
    int sign = 1;
    if(a < 0)
    {
        sign *= -1;
        a *= -1;
    }
    if(b < 0)
    {
        sign *= -1;
        b *= -1;
    }
    return sign * mulMatrix[a][b];
}

int convert(char c)
{
    switch(c)
    {
    case 'i':
    {
        return 2;
    }
    case 'j':
    {
        return 3;
    }
    case 'k':
    {
        return 4;
    }
    }
    return 0;
}
