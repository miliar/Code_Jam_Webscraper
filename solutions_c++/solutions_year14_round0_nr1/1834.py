#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int t;
    cin >> t;

    int *matches = new int[t], *card = new int[t];

    for (int i = 0; i < t; i++)
    {
        int a;
        cin >> a;

        int aarr[4][4];
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> aarr[j][k];

        int b;
        cin >> b;

        int barr[4][4];
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> barr[j][k];

        matches[i] = 0;
        card[i] = -1;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                if (aarr[a-1][j] == barr[b-1][k])
                {
                    matches[i]++;

                    if (matches[i] == 1)
                        card[i] =  aarr[a-1][j];
                }
    }

    for (int i = 0; i < t; i++)
    {
        if (matches[i] == 1)
            cout << "Case #" << (i+1) << ": " << card[i] << endl;
        else
            cout << "Case #" << (i+1) << ": " << (matches[i] == 0? "Volunteer cheated!": "Bad magician!") << endl;
    }

    delete[] matches;
    delete[] card;
}
