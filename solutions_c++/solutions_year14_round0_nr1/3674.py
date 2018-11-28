#include <iostream>
#include <map>
using namespace std;

int main()
{
    int T;
    int grid[4][4];
    int first;
    int second;
    map<int, int> values;
    bool found1 = false;
    bool found2 = false;
    int answer = -1;

    cin >> T;
    for(int val=1; val <= T; val++)
    {
        cin >> first;
        for(int i=0; i < 4; i++)
        {
            for(int j=0; j < 4; j++)
            {
                cin >> grid[i][j];
            }
        }

        for(int i=0; i < 4; i++)
        {
            values[ grid[first-1][i]]++;
        }

        cin >> second;
        for(int i=0; i < 4; i++)
        {
            for(int j=0; j < 4; j++)
            {
                cin >> grid[i][j];
            }
        }

        for(int i=0; i < 4; i++)
        {
            if(values[ grid[second-1][i] ] == 1)
            {
                if(!found1)
                {
                    answer = grid[second-1][i];
                    found1 = true;
                }
                else
                    found2 = true;
            }
        }

        if(!found1 && !found2)
            cout << "Case #" << val << ": Volunteer cheated!" << endl; 
        else if(found1 && !found2)
            cout << "Case #" << val << ": " << answer << endl;
        else if(found1 && found2)
            cout << "Case #" << val << ": Bad magician!" << endl;


        values.clear();
        found1 = false;
        found2 = false;
    }
    return 0;
}