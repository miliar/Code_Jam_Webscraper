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
#include <assert.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

#define mp make_pair
#define pb push_back

#define _USE_MATH_DEFINES
#define pi M_PI
#define endl '\n'

// using namespace __gnu_pbds;
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <vector<ll> > graph;
// typedef tree <ll,
//     null_type,
//     less <ll>,
//     rb_tree_tag,
//     tree_order_statistics_node_update> oset; // order_of_key, ...

int f(vector <int> &a)
{
    int sum = 0;
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] == 0)
            sum++;
    }
    return sum;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        int c, d, v;
        cin >> c >> d >> v;
        vector <int> pr(d);
        for (int i = 0; i < d; i++)
            cin >> pr[i];
        vector <int> a(v + 1, 0);
        a[0] = 1;
        for (int i = 0; i < (1 << d); i++)
        {
            int sum = 0;
            for (int j = 0; j < d; j++)
            {
                if (i & (1 << j))
                {
                    sum += pr[j];
                }
            }
            if (sum <= v)
                a[sum] = 1;
        }

        while (f(a) != 0)
        {
            for (int i = 0; i < a.size(); i++)
            {
                if (a[i] == 0)
                {
                    pr.pb(i);
                    break;
                }
            }
            for (int i = 0; i < (1 << (int)(pr.size())); i++)
            {
                int sum = 0;
                for (int j = 0; j < pr.size(); j++)
                {
                    if (i & (1 << j))
                    {
                        sum += pr[j];
                    }
                }
                if (sum <= v)
                    a[sum] = 1;
            }
        }
        cout << "Case #" << q + 1 << ": " << pr.size() - d << endl;
    }
    #ifdef HOME
        cerr << "\ntime = " << clock() / 1000 << " ms\n";
    #endif
    return 0;
}