#include <iostream>

using namespace std;

void readMatrix(char m[4][4]);

void printMatrix(char m[4][4])
{
    for (int i =0 ; i< 4; i++)
    {
        for (int j = 0; j< 4; j++)
        {
            cout << m[i][j];
        }
        cout << "\n";
    }
}

int checkRow(char m[4][4])
{
    for (int i = 0; i<4; i++)
    {
        int x=0, o=0;
        for (int j = 0; j < 4; j++)
        {
            if (m[i][j] == 'X')
                x++;
            if (m[i][j] == 'O')
                o++;
            if (m[i][j] == 'T')
                x++,o++;
        }
        if (x==4)
            return 1;
        if (o==4)
            return 2;
    }
}


int checkColumn(char m[4][4])
{
    for (int i = 0; i<4; i++)
    {
        int x=0, o=0;
        for (int j = 0; j < 4; j++)
        {
            if (m[j][i] == 'X')
                x++;
            if (m[j][i] == 'O')
                o++;
            if (m[j][i] == 'T')
                x++,o++;
        }
        if (x==4)
            return 1;
        if (o==4)
            return 2;
    }
}

int checkDiagonal(char m[4][4])
{
    int x=0, o=0;
    for (int i = 0; i<4; i++)
    {
        {
            if (m[i][i] == 'X')
                x++;
            if (m[i][i] == 'O')
                o++;
            if (m[i][i] == 'T')
                x++,o++;
        }
    }
    if (x==4)
        return 1;
    if (o==4)
        return 2;
             
    x=0, o=0;
    for (int i = 0; i<4; i++)
    {
        {
            if (m[i][3-i] == 'X')
                x++;
            if (m[i][3-i] == 'O')
                o++;
            if (m[i][3-i] == 'T')
                x++,o++;
        }
    }
    if (x==4)
        return 1;
    if (o==4)
        return 2;

}

bool hasEmptyCell (char m[4][4])
{
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
        {
            if (m[i][j] == '.')
                return true;
        }
    }
    return false;
}

int main()
{
    int n = 0;
    cin >> n;
    char m[4][4];
    for (int i = 0 ; i< n; i++)
    {
        readMatrix(m);
        int r = checkRow(m);
        if (r == 1) {
            cout << "Case #" <<i+1 << ": X won" <<endl;
            continue;
        }
        else if (r == 2) {
            cout << "Case #" <<i+1 << ": O won" <<endl;
            continue;
        }

        r = checkColumn(m);
        if (r == 1) {
            cout << "Case #" <<i+1 << ": X won" <<endl;
            continue;
        }
        else if (r == 2) {
            cout << "Case #" <<i+1 << ": O won" <<endl;
            continue;
        }

        r = checkDiagonal(m);
        if (r == 1) {
            cout << "Case #" <<i+1 << ": X won" <<endl;
            continue;
        }
        else if (r == 2) {
            cout << "Case #" <<i+1 << ": O won" <<endl;
            continue;
        }

        if (hasEmptyCell(m)) {
            cout << "Case #" <<i+1 << ": Game has not completed" <<endl;
        }
        else {
            cout << "Case #" <<i+1 << ": Draw" <<endl;
        }
    }
    return 0;
}

void readMatrix (char m[4][4]) 
{
    for (int i =0 ; i< 4; i++)
    {
        for (int j = 0; j< 4; j++)
        {
            char c;
            cin >> c;
            m[i][j] = c;
        }
    }
}
