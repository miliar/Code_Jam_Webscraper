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

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        long double c, f, x;
        cin >> c >> f >> x;
        
        long double p = 0.0;
        long double result = 1E200;

        forn(i, 5000000)
        {
            if (i > 0)
                p += c / (2 + (i - 1) * f);
            result = min(result, p + x / (2 + i * f));
        }

        cout << "Case #" << (tx + 1) << ": ";
        printf("%.10f\n", double(result));
    }
}

