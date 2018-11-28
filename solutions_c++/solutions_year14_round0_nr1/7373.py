#include <iostream>
#include <fstream>
using namespace std;

int findSame(int p1[4], int p2[4])
{
    int s = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            if (p1[i] == p2[j])
            {
                if (s > 0 || s == -1)
                    s = -1;
                else
                    s = p1[i];
            }
        }
    if (s == 0)
        return -2;
    else
        return s;
}

int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-attempt1.out");
    int times = 0;
    int guess = 0;
    int cards[4][4];
    int cards1[4];
    int cards2[4];
    int tmp = 0;
    int i, j, t;
    int result;

    fin >> times;

    for (t = 0; t < times; ++t)
    {
        fin >> guess;
        for (i = 0; i < 4; ++i)
            for (j = 0; j < 4; ++j)
                fin >> cards[i][j];

        for (j = 0; j < 4; ++j)
            cards1[j] = cards[guess-1][j];

    fin >> guess;
        for (i = 0; i < 4; ++i)
            for (j = 0; j < 4; ++j)
                fin >> cards[i][j];

        for (j = 0; j < 4; ++j)
            cards2[j] = cards[guess-1][j];

        result = findSame(cards1, cards2);

        if (result > 0)
            fout << "Case #" << (t+1) << ": " << result << endl;
        else if (result == -1)
            fout << "Case #" << (t+1) << ": Bad magician!" << endl;
        else if (result == -2)
            fout << "Case #" << (t+1) << ": Volunteer cheated!" << endl;
    }
    fin.close();
    fout.close();
}
