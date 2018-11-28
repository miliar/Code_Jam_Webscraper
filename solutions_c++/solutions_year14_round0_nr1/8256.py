#include<iostream>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<fstream>

using namespace std;
int main()
{
    int n, r1, r2, x[4][4], y[4][4];
    ifstream cin("A-small-attempt0.in");
    ofstream cout("a.out");
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> r1;
        r1--;
        for (int j = 0; j < 16; j++)
        {
            cin >> x[j / 4][j % 4];
        }
        cin >> r2;
        r2--;
        for (int j = 0; j < 16; j++)
        {
            cin >> y[j / 4][j % 4];
        }
        vector<int> v1, v2, res(8);
        v1.push_back(x[r1][0]);
        v1.push_back(x[r1][1]);
        v1.push_back(x[r1][2]);
        v1.push_back(x[r1][3]);

        v2.push_back(y[r2][0]);
        v2.push_back(y[r2][1]);
        v2.push_back(y[r2][2]);
        v2.push_back(y[r2][3]);

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        auto it = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), res.begin());
        res.resize(it - res.begin());
        if (res.size() > 1)
        {
            cout << "Case #" << i << ": Bad magician!\n";
        } 
        else if (res.size() == 1)
        {
            cout << "Case #" << i << ": " << res[0] << "\n";
        }
        else
        {
            cout << "Case #" << i << ": Volunteer cheated!\n";
        }
    }

}