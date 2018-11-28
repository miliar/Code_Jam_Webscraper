#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define int long long

using namespace std;

main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int x, n;
        cin >> x >> n;
        int A[n];

        for (int i = 0; i < n; i++)
            cin >> A[i];
        sort(A, A + n);
        int res = n;
        int add = 0;
        int pr_x = x;
        
        while (n >= 0)
        {
            int counter = 0;
            x = pr_x;

            for (int i = 0; i < n; i++)
            {
                if (A[i] < x)
                    x += A[i];
                else
                {
                    if (x - 1 == 0)
                    {
                        counter = n;
                        break;
                    }

                    while (x <= A[i])
                    {
                        x += x - 1;
                        counter++;
                    }
                    x += A[i];
                }
            }
            res = min(res, counter + add);
            n--;
            add++;
        }
        printf("Case #%d: %d\n", t + 1, res);
    }
}
