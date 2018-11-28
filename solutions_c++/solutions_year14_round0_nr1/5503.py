/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License: GNU GPL
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int t, first, second;
int firstArrangement[4][4];
int secondArrangement[4][4];
int flags[20];

void Solve(int num)
{
    int firstTrue = first - 1;
    int secondTrue = second - 1;

    for(int i = 0; i < 4; ++i)
    {
        flags[firstArrangement[firstTrue][i]] = 1;
    }

    int ans = 0;
    int res = 0;

    for(int i = 0; i <4; ++i)
    {
        if(flags[secondArrangement[secondTrue][i]])
        {
            if(res == 0) res = secondArrangement[secondTrue][i];
            ans++;
        }
    }

    cout << "Case #" << num << ": ";

    if(ans == 0)
    {
        cout << "Volunteer cheated!" << endl;
    }
    else if(ans == 1)
    {
        cout << res << endl;
    }
    else cout << "Bad magician!" << endl;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-res.out", "w", stdout);
    cin >> t;
    int tFirst = t;
    while(t--)
    {
        memset(flags, 0, sizeof(flags));
        cin >> first;
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> firstArrangement[i][j];
            }
        }
        cin >> second;
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> secondArrangement[i][j];
            }
        }
        Solve(tFirst - t);
    }

    return 0;
}
