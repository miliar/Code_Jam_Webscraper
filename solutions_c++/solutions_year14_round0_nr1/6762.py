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
        cout << "Case #" << q + 1 << ": ";
        int a;
        cin >> a;
        int A[16];
        vector <int> V;
        a--;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                int k;
                cin >> k;
                k--;
                A[k] = i;
            }
        }
        int b;
        cin >> b;
        b--;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                int k;
                cin >> k;
                k--;
                if (b == i && A[k] == a)
                    V.pb(k + 1);
            }
        }
        if ((int)V.size() == 0)
        {
            cout << "Volunteer cheated!";
        }
        else if ((int)V.size() != 1)
        {
            cout << "Bad magician!";
        }
        else
        {
            cout << V[0];
        }
        cout << endl;
    }

    return 0;
}
