#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int a[4][4];
int T, x, o;
bool isContinue, isFull, isEnd;

void judge(int j, int k)
{
    switch (a[j][k])
    {
    case '.':
        isContinue = false;
        isFull = false;
        break;

    case 'T':
        ++x;
        ++o;
        break;

    case 'X':
        ++x;
        break;

    case 'O':
        ++o;
        break;
    }
}

int main()
{
    ofstream cout("data.out");
    string t;
    int i, j, k;
    cin >> T;

    for (i = 1; i <= T; ++i)
    {
        isFull = true;
        isEnd = false;
        for (j = 0; j < 4; ++j)
        {
            cin >> t;
            for (k = 0; k < 4; ++k)
                a[j][k] = t[k];
        }

        x = o = 0;
        judge(0, 0);
        judge(1, 1);
        judge(2, 2);
        judge(3, 3);
        if (4 == x)
        {
            isEnd = true;
            cout << "Case #" << i << ": X won" << endl;
        }
        else if (4 == o)
        {
            isEnd = true;
            cout << "Case #" << i << ": O won" << endl;
        }

        if (isEnd)
            continue;
        x = o = 0;
        judge(0, 3);
        judge(1, 2);
        judge(2, 1);
        judge(3, 0);
        if (4 == x)
        {
            isEnd = true;
            cout << "Case #" << i << ": X won" << endl;
        }
        else if (4 == o)
        {
            isEnd = true;
            cout << "Case #" << i << ": O won" << endl;
        }

        if (isEnd)
            continue;
        for (j = 0; j < 4; ++j)
        {
            x = o = 0;
            isContinue = true;
            for (k = 0; k < 4; ++k)
            {
                if (!isContinue)
                    break;

                judge(j, k);
            }
            if (4 == x)
            {
                isEnd = true;
                cout << "Case #" << i << ": X won" << endl;
                break;
            }
            else if (4 == o)
            {
                isEnd = true;
                cout << "Case #" << i << ": O won" << endl;
                break;
            }
        }

        if (isEnd)
            continue;
        for (k = 0; k < 4; ++k)
        {
            x = o = 0;
            isContinue = true;
            for (j = 0; j < 4; ++j)
            {
                if (!isContinue)
                    break;

                judge(j, k);
            }
            if (4 == x)
            {
                isEnd = true;
                cout << "Case #" << i << ": X won" << endl;
                break;
            }
            else if (4 == o)
            {
                isEnd = true;
                cout << "Case #" << i << ": O won" << endl;
                break;
            }
        }

        if (isEnd)
            continue;
        if (isFull)
            cout << "Case #" << i << ": Draw" << endl;
        else
            cout << "Case #" << i << ": Game has not completed" << endl;
    }

    return 0;
}
