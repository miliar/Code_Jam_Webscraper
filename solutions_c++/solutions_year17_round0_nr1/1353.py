#include <iostream>
#include <queue>

using namespace std;

void flip(char &c) {
    c = (c == '+' ? '-' : '+');
}

int get_side(char c) {
    return c == '+' ? 1 : 0;
}

int solve(string &s, int n) {
    int ans = 0;
    queue<int> q;
    for (int i = 0; i < (int)s.size(); ++i) {
        while (!q.empty()) {
            if (q.front() < i)
                q.pop();
            else
                break;
        }

        if ( (get_side(s[i]) ^ (q.size() & 1) ) == 0  && i + n - 1 < (int)s.size()) {
            ++ans;
            q.push(i + n - 1);
        }
        if (q.size() & 1)
            flip(s[i]);
    }

    for (int i = (int)s.size() - n + 1; i < (int)s.size(); ++i) {
        if ( get_side(s[i]) == 0 )
            return -1;
    }

    return ans;
}

int main()
{
    freopen("in2.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        string s;
        int n;
        cin >> s >> n;

        int ans = solve(s, n);
        cout << "Case #" << i << ": " << (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << "\n";
    }

    return 0;
}
