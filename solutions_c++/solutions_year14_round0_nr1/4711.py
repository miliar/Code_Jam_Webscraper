#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int idx = 1; idx <= t; idx++)
    {
        cout << "Case #" << idx << ": ";
        int first_row, second_row;
        int m[4][4] = {0}, n[4][4] = {0};
        cin >> first_row;
        for (int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> m[i][j];
        cin >> second_row;
        for (int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> n[i][j];
        first_row--;
        second_row--;
        int cnt = 0, hited = 0;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (m[first_row][i] == n[second_row][j])
                {
                    cnt++;
                    hited = m[first_row][i];
                }
            }
        }
        if(cnt == 0)
            cout << "Volunteer cheated!" << endl;
        else if (cnt >= 2)
            cout << "Bad magician!" << endl;
        else
            cout << hited << endl;
    }
    return 0;
}
