#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int cts, ans1, ans2, n, found, num;
    vector<int> row1;

    cin >> cts;
    for(int ct = 1; ct <= cts; ct++)
    {
        row1.clear();
        found = 0;

        cin >> ans1;
        //cout << "Row: " << ans1 << endl;
        //cout << ">> ";
        for(int i = 0; i < (ans1 - 1)*4; i++)
        {
            cin >> n;
            //cout << n << " ";
        }
        //cout << endl;

        for(int i = 0; i < 4; i++)
        {
            cin >> n;
            //cout << n << " ";
            row1.push_back(n);
        }
        //cout << endl;

        //cout << ">> ";
        for(int i = 0; i < (4 - ans1)*4; i++)
        {
            cin >> n;
            //cout << n << " ";
        }
        //cout << endl << endl;

        cin >> ans2;
        //cout << "Row: " << ans2 << endl;
        //cout << ">> ";
        for(int i = 0; i < (ans2 - 1)*4; i++)
        {
            cin >> n;
            //cout << n << " ";
        }
        //cout << endl;

        for(int i = 0; i < 4; i++)
        {
            cin >> n;
            if(find(row1.begin(), row1.end(), n) != row1.end())
            {
                num = n;
                found++;
            }
            //cout << n << " ";
        }
        //cout << endl;

        //cout << ">> ";
        for(int i = 0; i < (4 - ans2)*4; i++)
        {
            cin >> n;
            //cout << n << " ";
        }
        //cout << endl;

        cout << "Case #" << ct << ": ";
        if(found >= 2)
            cout << "Bad magician!" << endl;
        else if(found == 0)
            cout << "Volunteer cheated!" << endl;
        else
            cout << num << endl;
    }

    return 0;
}

