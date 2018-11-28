#include <iostream>
#include <set>
#include <vector>
#include <cstdio>

using namespace std;

int grid1[16][16], grid2[16][16];

int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);
    int ans1, ans2;
    int nbT;
    cin >> nbT;
    for (int t = 1; t <= nbT; t++)
    {
        cin >> ans1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> grid1[i][j];
        cin >> ans2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> grid2[i][j];

        vector<int> sol;
        set<int> present;
        int lin = ans1-1;
        for (int i = 0; i < 4; i++)
            present.insert(grid1[lin][i]);
        lin = ans2-1;
        for (int i = 0; i < 4; i++)
            if (present.find(grid2[lin][i]) != present.end())
                sol.push_back(grid2[lin][i]);

        cout << "Case #" << t << ": ";
        if (sol.size() == 0)
            cout << "Volunteer cheated!\n";
        else if (sol.size() > 1)
            cout << "Bad magician!\n";
        else
            cout << sol[0] << '\n';


    }
    return 0;
}
