#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
typedef unsigned long long ull;

bool get_sol(vector<ull>& sol, int k, int c, int s)
{
    // for the small dataset, if s == k, we can always choose only the first k
    if (s == k)
    {
        for (int i = 1; i <= k; i ++)
            sol.push_back(i);
        return true;
    }

    return false;
}

void solve(int test_nr)
{
    int k,c,s;
    cin >> k >> c >> s;

    vector<ull> sol;
    bool possible = get_sol(sol,k,c,s);

    cout << "Case #" << test_nr << ":";
    if (possible) {
        for (int i = 0; i < sol.size(); i ++)
            cout << " " << sol[i];
    } else {
        cout << " IMPOSSIBLE";
    }
    cout << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i ++) {
        solve(i);
    }

    return 0;
}
