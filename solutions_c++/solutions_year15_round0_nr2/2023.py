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
    
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        int d;
        cin >> d;
        vector <int> v(d);
        int m = -1;
        for (int i = 0; i < d; i++)
        {
            cin >> v[i];
            m = max(v[i], m);
        }
        int ans = m;
        for (int i = 2; i < m; i++)
        {
            int cnt = 0;
            for (int j = 0; j < d; j++)
                cnt += (v[j] + i - 1) / i - 1;
            ans = min(ans, cnt + i);
        }
        cout << "Case #" << q + 1 << ": " << ans << endl;
    }
    #ifdef HOME
        cerr << "\ntime = " << clock() / 1000 << " ms\n";
    #endif
    return 0;
}