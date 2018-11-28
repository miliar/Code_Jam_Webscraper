#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

int ma [200][200];
int maxR [200];
int maxC [200];

int main (){

    int n, m, T;

    freopen ("B-large.in","r",stdin);
    freopen ("b.out","w",stdout);

    cin >> T;

    for (int tc = 0 ; tc < T ; tc ++)
    {
        cin >> n >> m;
        memset (maxR, 0, sizeof (maxR));
        memset (maxC, 0, sizeof (maxC));

        for (int i = 0 ; i < n ; i ++)
        {
            for (int j = 0 ; j < m ; j ++)
            {
                cin >> ma [i][j];
                maxR [i] = max (maxR [i], ma [i][j]);
                maxC [j] = max (maxC [j], ma [i][j]);
            }
        }

        bool flag = true;

        for (int i = 0 ; i < n ; i ++)
        {
            for (int j = 0 ; j < m ; j ++)
            {
                if (ma [i][j] < maxR [i] && ma [i][j] < maxC [j])
                {
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
        }

        if (flag)
        {
            cout << "Case #" << tc + 1 << ": YES" << endl;
        }else
        {
            cout << "Case #" << tc + 1 << ": NO" << endl;
        }
    }

    return 0;
}
