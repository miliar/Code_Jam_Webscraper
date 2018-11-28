// License {{{
// Copyright © 2016 Fedor Alekseev <feodor.alexeev@gmail.com>
// This work is free. You can redistribute it and/or modify it under the
// terms of the Do What The Fuck You Want To Public License, Version 2,
// as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
// }}}

#include <bits/stdc++.h>
using namespace std;

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC)

#define hot(x) (x)
#define sweet(value) (value)
#define faceless

#define WHOLE(v) (v).begin(),(v).end()
#define RWHOLE(v) (v).rbegin(),(v).rend()
#define UNIQUE(v) (v).erase(unique(WHOLE(v)),(v).end())

typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

typedef array<int, 3> State;

const string letters = "PRS";

bool beats(int a, int b)
{
    return (a + 1) % 3 == b;
}

string doit(int target, State& cur, int level)
{
    if (level == 0)
    {
        if (cur[target] == 0)
            return "";
        --cur[target];
        return letters.substr(target, 1);
    }

    string left = doit(target, cur, level - 1);
    if (left.empty())
        return left;
    string right = doit((target + 1) % 3, cur, level - 1);
    if (right.empty())
        return right;

    return min(left + right, right + left);
}

void solve()
{
    int n;
    State init;
    cin >> n >> init[1] >> init[0] >> init[2];

    vector<string> answers;
    for (int i = 0; i < 3; ++i)
    {
        State state = init;
        string here = doit(i, state, n);
        if (!here.empty())
            answers.push_back(here);
    }

    if (answers.empty())
        cout << "IMPOSSIBLE\n";
    else
        cout << *min_element(WHOLE(answers)) << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}

