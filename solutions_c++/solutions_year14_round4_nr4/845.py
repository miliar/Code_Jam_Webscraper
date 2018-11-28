#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stdint.h>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <stack>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define foreach(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define sz(v) int((v).size())


void rec(int step, int strings_count, int servers_count,
         const vector < string > & strings,
         vector < int > & history,
         ll & result, ll & max_nodes)
{
    if(step == strings_count)
    {
        vector < set < string > > sets(servers_count);
        for(int i = 0; i < strings_count; i++)
        {
            for(int j = 1; j <= strings[i].size(); j++)
            {
                string substring = strings[i].substr(0, j);
                sets[history[i]].insert(substring);
            }
        }
        ll current_nodes = 0;
        for(int i = 0; i < servers_count; i++)
        {
            if(!sets[i].empty())
                current_nodes += sets[i].size() + 1;
        }
        if(current_nodes == max_nodes)
        {
            result += 1;
        }
        else if(current_nodes > max_nodes)
        {
            max_nodes = current_nodes;
            result = 1;
        }
    }
    else
    {
        for(int i = 0; i < servers_count; i++)
        {
            history[step] = i;
            rec(step + 1, strings_count, servers_count, strings, history, result, max_nodes);
        }
    }
}

pair < ll, ll > solve_dumb(int strings_count, int servers_count,
                     const vector < string > & strings)
{
    ll result = 0, max_nodes = 0;
    vector < int > history(strings_count, 0);
    rec(0, strings_count, servers_count, strings,
        history,
        result, max_nodes);
    return mp(result, max_nodes);
}

void solve()
{
    int strings_count, servers_count;
    cin >> strings_count >> servers_count;
    vector < string > strings(strings_count);
    for(int i = 0; i < strings_count; i++)
        cin >> strings[i];
    pair < ll, ll > result = solve_dumb(strings_count, servers_count, strings);
    cout << result.second << " " << result.first << endl;
}

int main()
{
    int tests;
    cin >> tests;
    for(int test = 1; test <= tests; test++)
    {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}