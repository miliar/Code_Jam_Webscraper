#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("data.out");

    int t;
    fin >> t;
    for (int i = 0; i < t; ++i)
    {
        int c1, c2;
        int arr[4][4],arr2[4][4];

        fin >> c1;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                fin >> arr[j][k];

        fin >> c2;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                fin >> arr2[j][k];

        bool used1[17] = {false};
        bool used2[17] = {false};

        for (int j = 0; j < 4; ++j)
            used1[arr[c1 - 1][j]] = true;

        for (int j = 0; j < 4; ++j)
            used2[arr2[c2 - 1][j]] = true;

        bool ans = false;
        bool badMag = false;
        int sol;
        for (int j = 1; j <= 16; ++j)
        {
            if (used1[j] == true && used2[j] == true && !ans)
            {
                sol = j;
                ans = true;
            }
            else if (used1[j] == true && used2[j] == true && ans && !badMag)
            {
                badMag = true;
            }
        }

        if (badMag)
        {
            fout << "Case #" << i + 1 << ": Bad magician!" << endl;
        }
        else if (!ans)
        {
            fout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        }
        else
        {
            fout << "Case #" << i + 1 << ": " << sol << endl;
        }
    }

    fin.close();
    fout.close();

    return 0;
}
