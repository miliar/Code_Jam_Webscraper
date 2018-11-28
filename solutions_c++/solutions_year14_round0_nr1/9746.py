#include <iostream>
#include <vector>
#include <set>

using namespace std;

int
main()
{
    vector< vector<int> > M1 (4,vector<int>(4,0));
    vector < set<int> > M2 (4, set<int>());
    int T, f1, f2, c, d, i, j, r;
    bool encontrado, mal;

    cin >> T;

    for (c = 0; c < T; ++c)
    {
        cin >> f1;
        --f1;

        for (i = 0; i < 4;++i)
        {
            for (j = 0; j < 4; ++j)
            {
                cin >> d;
                M1[i][j] = d;
            }
        }

        cin >> f2;
        --f2;

        for (i = 0; i < 4;++i)
        {
            for (j = 0; j < 4; ++j)
            {
                cin >> d;
                M2[i].insert(d);
            }
        }

        encontrado = false;
        mal = false;
        for (i = 0; i < 4; ++i)
        {
            if ( M2[f2].find(M1[f1][i]) != M2[f2].end() )
            {
                if (!encontrado)
                {
                    encontrado = true;
                    r = M1[f1][i];
                }
                else
                {
                    mal = true;
                    break;
                }
            }
        }
        if (!encontrado)
        {
            cout << "Case #" << c+1 << ": Volunteer cheated!" << endl;
        }
        else if (encontrado && mal)
        {
            cout << "Case #" << c+1 << ": Bad magician!" << endl;
        }
        else
        {
            cout << "Case #" << c+1 << ": " << r << endl;
        }

        for (i = 0; i < 4;++i)
        {
            M2[i].clear();
        }
    }

    return 0;
}
