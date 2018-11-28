#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <queue>
#include <vector>
using namespace std;

typedef vector<int> state;
string toStr(const state& s)
{
    string res;
    res.reserve(s.size());
    for (auto n: s)
        res.push_back(n);
    return res;
}

bool isFinal(const state& s)
{
    for (auto n: s)
        if (n != 0)
            return false;
    return true;
}

int bfs(const state& s0)
{
    set<string> visited;
    visited.insert(toStr(s0));

    queue<pair<state, int>> q;
    q.push(make_pair(s0, 0));

    while (true)
    {
        const auto& top = q.front();
        const auto& state = top.first;
        auto len = top.second;

        if (isFinal(state))
            return len;

        auto decremented = state;
        for (auto& n: decremented)
            if (n > 0)
                --n;
        std::sort(decremented.begin(), decremented.end());
        auto decrementedStr = toStr(decremented);
        if (visited.find(decrementedStr) == visited.end())
        {
            visited.insert(decrementedStr);
            q.push(make_pair(decremented, len + 1));
        }

        for (auto i = 0u; i < state.size(); ++i)
        {
            for (int k = 1; k < state[i]; ++k)
            {
                auto newState = state;
                newState[i] -= k;
                newState.push_back(k);
                std::sort(newState.begin(), newState.end());

                auto str = toStr(newState);
                if (visited.find(str) != visited.end())
                    continue;

                visited.insert(str);
                q.push(make_pair(newState, len + 1));
            }
        }

        q.pop();
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;

    state s;
    for (int i = 1; i <= T; ++i)
    {
        s.clear();
        int D;
        cin >> D;
        for (int i = 0; i < D; ++i)
        {
            int p; cin >> p;
            s.push_back(p);
        }

        cout << "Case #" << i << ": " << bfs(s) << '\n';
    }
    cout.flush();
}
