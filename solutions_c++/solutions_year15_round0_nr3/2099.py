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

string mul(string a, char b)
{
    if (a == "1" && b == 'i')
        return "i";
    if (a == "1" && b == 'j')
        return "j";
    if (a == "1" && b == 'k')
        return "k";

    if (a == "-1" && b == 'i')
        return "-i";
    if (a == "-1" && b == 'j')
        return "-j";
    if (a == "-1" && b == 'k')
        return "-k";


    if (a == "i" && b == 'i')
        return "-1";
    if (a == "i" && b == 'j')
        return "k";
    if (a == "i" && b == 'k')
        return "-j";


    if (a == "-i" && b == 'i')
        return "1";
    if (a == "-i" && b == 'j')
        return "-k";
    if (a == "-i" && b == 'k')
        return "j";


    if (a == "j" && b == 'i')
        return "-k";
    if (a == "j" && b == 'j')
        return "-1";
    if (a == "j" && b == 'k')
        return "i";

    if (a == "-j" && b == 'i')
        return "k";
    if (a == "-j" && b == 'j')
        return "1";
    if (a == "-j" && b == 'k')
        return "-i";


    if (a == "k" && b == 'i')
        return "j";
    if (a == "k" && b == 'j')
        return "-i";
    if (a == "k" && b == 'k')
        return "-1";

    if (a == "-k" && b == 'i')
        return "-j";
    if (a == "-k" && b == 'j')
        return "i";
    if (a == "-k" && b == 'k')
        return "1";

    return "lol";
}

string dp[10000][10000];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        int l, x;
        cin >> l >> x;
        string s, ss;
        cin >> s;
        ss = s;
        for (int i = 0; i < x - 1; i++)
            s += ss;
        int n = s.size();
        for (int i = 0; i < n; i++)
            dp[i][i] = s[i];
        for (int len = 2; len <= n; len++)
        {
            for (int st = 0; st < n; st++)
            {
                if (st + len - 1 < n)
                {
                    dp[st][st + len - 1] = mul(dp[st][st + len - 2], s[st + len - 1]);
                }
            }
        }
        bool ok = 0;
        for (int i = 1; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (dp[0][i - 1] == "i" && dp[i][j - 1] == "j" && dp[j][n - 1] == "k")
                {
                    ok = 1;
                    break;
                }
            }
        }
        cout << "Case #" << q + 1 << ": " << (ok ? "YES" : "NO") << endl;
        cerr << "Case #" << q + 1 << ": " << (ok ? "YES" : "NO") << endl;
    }
    #ifdef HOME
        cerr << "\ntime = " << clock() / 1000 << " ms\n";
    #endif
    return 0;
}