#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int index = 1; index <= t; ++index)
    {
        int n;
        cin >> n;

        double *naomi = new double[ n ];
        double *ken   = new double[ n ];

        for(int i = 0; i < n; ++i)
        {
            cin >> naomi[ i ];
        }

        for(int i = 0; i < n; ++i)
        {
            cin >> ken[ i ];
        }

        sort(naomi, naomi + n);
        sort(ken, ken + n);

        int res1 = 0;
        int flag = ken[ n - 1 ] == 1;

        for(int i = flag, j = 0, maxj = n - flag; i < n, j < maxj; ++i)
        {
            if(naomi[ i ] > ken[ j ])
            {
                ++res1;
                ++j;
            }
            else
            {
                maxj -= 1;
            }
        }

        int res2 = 0;
        for(int i = 0, j = 0; i < n and j < n; ++i, ++j)
        {
            while(j < n and ken[ j ] < naomi[ i ])
            {
                ++j;
                ++res2;
            }
        }

        cout << "Case #" << index << ": " << res1 << ' ' << res2 << endl;

        delete [] naomi;
        delete [] ken;
    }
}
