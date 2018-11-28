#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define RI(x) scanf("%d", &x)
#define RL(x) scanf("%I64d", &x)
#define RD(x) scanf("%f", &x)

string s;
deque<char> q;

void solve(int case_number)
{
    cin >> s;
    q.clear();
    q.push_back(s[0]);
    for (int i=1; i<s.length(); ++i)
    {
        if (s[i] < q.front())
            q.push_back(s[i]);
        else
            q.push_front(s[i]);
    }
    cout << "Case #" << case_number << ": ";
    while (!q.empty())
    {
        cout << q.front();
        q.pop_front();
    }
    cout << "\n";
}

int main()
{
    freopen("input1.in", "r", stdin);
    freopen("output1.out", "w", stdout);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)
        solve(i);

    return 0;
}

