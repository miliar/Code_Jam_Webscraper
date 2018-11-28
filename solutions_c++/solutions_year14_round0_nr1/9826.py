#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    int t;
    int ans;
    int tab[4][4];
    int choose[4];

    cin >> t;

    for (int i = 0 ; i < t ; i++)
    {
        cin >> ans;
        ans--;

        for (int j = 0 ; j < 4 ; j++)
        {
            for (int k = 0 ; k < 4 ; k++)
            {
                cin >> tab[j][k];
                if (j == ans)
                    choose[k] = tab[j][k];
            }
        }

        cin >> ans;
        ans--;
        int count = 0;
        int target;

        for (int j = 0 ; j < 4 ; j++)
        {
            for (int k = 0 ; k < 4 ; k++)
            {
                cin >> tab[j][k];
                if (j == ans)
                {
                    if (find(choose, choose+4, tab[j][k]) != choose+4)
                    {
                        count++;
                        target = tab[j][k];
                    }
                }
            }
        }

        cout << "Case #" << i+1 << ": ";
        
        if (count == 1)
            cout << target << endl;
        else if (count > 1)
            cout << "Bad magician!" << endl;
        else
            cout << "Volunteer cheated!" << endl;
    }

    exit(EXIT_SUCCESS);
}
