#include <set>
#include <iostream>

using namespace std;

int solve(multiset<int>& S, int X)
{
    int ans = 0;
    while (!S.empty())
    {
        ++ans;
        multiset<int>::iterator itLast = S.end();
        --itLast;
        int largest = *itLast;
        S.erase(itLast);
        multiset<int>::iterator itBuddy = S.upper_bound(X - largest);
        if (itBuddy != S.begin())
        {
            --itBuddy;
            S.erase(itBuddy);
        }
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N, X;
        cin >> N >> X;
        multiset<int> S;
        for (int i = 0; i < N; ++i)
        {
            int s;
            cin >> s;
            S.insert(s);
        }
        int ans = solve(S, X);
        cout << "Case #" << testcase << ": " << ans << "\n";
    }
    return 0;
}
