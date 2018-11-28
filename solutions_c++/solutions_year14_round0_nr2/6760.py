#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <deque>
#include <stack>
#include <string>
#include <ctime>
#include <list>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <queue>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

#define mp make_pair
#define pb push_back

#define _USE_MATH_DEFINES
#define pi M_PI

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <vector<int> > graph;

int main()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int q = 0; q < T; q++)
    {
        cerr << "Test # " << q + 1 << endl;
        cout << "Case #" << q + 1 << ": ";
        ld c, f, x;
        cin >> c >> f >> x;
        ld ANS = 1e14;
        for (int i = 0; i < 10000; i++)
        {
            ld t = 0;
            ld dx = 2;
            for (int j = 0; j < i; j++)
            {
                t += c / dx;
                dx += f;
            }
            t += x / dx;
            ANS = min(t, ANS);
        }
        cout.precision(20);
        cout << ANS;
        cout << endl;
    }

    return 0;
}
