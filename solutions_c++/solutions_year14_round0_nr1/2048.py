#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

set<int> readset()
{
    int row;
    set<int> res;
    cin >> row;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            int c;
            cin >> c;
            if (i == row-1)
                res.insert(c);
        }
    }
    return res;
}

void solve(int t)
{
    set<int> a = readset();
    set<int> b = readset();
    int res, numres = 0;
    for (set<int>::iterator itr = a.begin(); itr != a.end(); itr++)
    {
        if (b.count(*itr) > 0)
        {
            res = *itr;
            numres++;
        }
    }

    cout << "Case #" << t+1 << ": ";
    if (numres == 0)
        cout << "Volunteer cheated!" << endl;
    if (numres > 1)
        cout << "Bad magician!" << endl;
    if (numres == 1)
        cout << res << endl;

}

int main(int argc, char *argv[])
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve(i);

    return 0;
}
