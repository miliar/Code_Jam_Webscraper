#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main()
{
    FILE *fin = freopen("D-small.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("D-small.out", "w", stdout);
    int tries, K, C, S;
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> K;
        cin >> C;
        cin >> S;
        vector <int> arr;
        if (C > 1)
        {
            int cntr = ceil(K/2.0);
            int k = K;
            if (S >= cntr)
            {
                for (int l = 0; l < cntr; l++)
                {
                    arr.push_back(k);
                    k += (K-1);
                }
            }
        }
        else
        {
            if (S >= K)
            {
                for (int l = 1; l <= K; l++)
                    arr.push_back(l);
            }
        }
        cout << "Case #" << i << ": ";
        if (arr.size() == 0)
            cout << "IMPOSSIBLE" << endl;
        else
        {
            for (int m = 0; m < arr.size(); m++)
                cout << arr[m] << " ";
            cout << endl;
        }
    }
    return 0;
}
