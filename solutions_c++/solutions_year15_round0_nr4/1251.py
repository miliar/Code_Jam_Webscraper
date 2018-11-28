#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=1; i <= t; ++i)
    {
        bool canDo = false;
        int x, r, c;
        cin >> x >> r >> c;

        if(x == 1)
            canDo = true;
        else if(x == 2)
            canDo = (r % 2 == 0 || c % 2 == 0);
        else if(x == 3)
            canDo = (r * c > 3 && r * c % 3 == 0);
        else if(x == 4)
            canDo = (r * c >= 12);

        cout << "Case #" << i << ": " << ( canDo ? "GABRIEL" : "RICHARD") << endl;
    }

    return 0;
}
