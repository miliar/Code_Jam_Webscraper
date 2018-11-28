//codejam2014-A-small
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);

    int T, case_number = 1;

    cin >> T;

    while (T--)
    {
        int row, x;

        set<int> set1, set2, result;

        cin >> row;

        for (int i=0; i<4; ++i)
        {
            for (int j=0; j<4; ++j)
            {
                cin >> x;

                if (i+1 == row)
                    set1.insert(x);
            }
        }

        cin >> row;

        for (int i=0; i<4; ++i)
        {
            for (int j=0; j<4; ++j)
            {
                cin >> x;

                if (i+1 == row)
                    set2.insert(x);
            }
        }

        set_intersection(set1.begin(), set1.end(),
                         set2.begin(), set2.end(),
                         inserter(result, result.begin()));

        cout << "Case #" << case_number++ << ": ";

        if (result.size() == 1)
            cout << *result.begin();
        else if (result.size() == 0)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";

        cout << endl;
    }

    return 0;
}