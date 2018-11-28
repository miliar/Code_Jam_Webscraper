#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

typedef long long li;

int n;
vector<li> a;

void readData()
{
    li p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    a = vector<li>(n);
    forn(i, n)
        a[i] = ((i * p + q) % r) + s;
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    int fromTest = 1;
    int toTest = tt;

    if (argc == 3)
    {
        fromTest = atoi(argv[1]);
        toTest = atoi(argv[2]);
    }

    cerr << "Solving " << fromTest << " ... " << toTest << endl;

    for (int tx = 1; tx <= tt; tx++)
    {
        readData();
        if (tx >= fromTest && tx <= toTest)
        {
            vector<li> sum(n + 1);
            forn(i, n)
                sum[i + 1] = sum[i] + a[i];

            long double result = 0.0;

            forn(i, n)
            {
                li lf = sum[i];

                int l = i;
                int r = n - 1;

                while (r - l > 100)
                {
                    int mid = (r + l) / 2;

                    li a = sum[mid + 1] - sum[i];
                    li b = sum[n] - sum[mid + 1];

                    if (a <= b)
                        l = mid;
                    else
                        r = mid;
                }

                // cout << sum[n] << endl;

                //for (int mid = i; mid <= n - 1; mid++)
                for (int mid = l; mid <= r; mid++)
                {
                    li a = sum[mid + 1] - sum[i];
                    li b = sum[n] - sum[mid + 1];

                    result = max(result, (long double)(sum[n] - max(lf, max(a, b))) / (long double)(sum[n]));
                }
            }

            cerr << tx << endl;
            cout << "Case #" << (tx) << ": ";
            printf("%.10lf\n", double(result));
        }
    }
}
