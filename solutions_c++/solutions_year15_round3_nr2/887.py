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

int k, l, s;
string let, res;

string TMP;

ld SUM = 0;
int maxx = 0;

void check()
{
    int cnt = 0;
    for (int i = 0; i < s; i++)
    {
        if (i + res.size() - 1 >= s)
            break;
        bool ok = 1;
        for (int j = 0; j < res.size(); j++)
        {
            if (res[j] != TMP[i + j])
            {
                ok = 0;
                break;
            }
        }
        if (ok)
        {
            cnt++;
        }
    }
    maxx = max(maxx, cnt);
    SUM += cnt;
    // cout << TMP << " " << res << " " << cnt << endl;
}

void gen(int pos)
{
    if (pos == s)
    {
        check();
        return;
    }
    for (int i = 0; i < k; i++)
    {
        TMP += let[i];
        gen(pos + 1);
        TMP.pop_back();
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        cin >> k >> l >> s >> let >> res;
        TMP = "";
        SUM = 0;
        maxx = 0;
        gen(0);
        ld st = 1;
        for (int i = 0; i < s; i++)
            st *= k;
        cout.precision(20);
        cout << fixed << "Case #" << q + 1 << ": " << (ld)maxx - ((ld)1 / (st)) * SUM << endl;
    }
    #ifdef HOME
        cerr << "\ntime = " << clock() / 1000 << " ms\n";
    #endif
    return 0;
}