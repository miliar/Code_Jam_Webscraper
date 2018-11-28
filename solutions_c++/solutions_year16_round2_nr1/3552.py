#include <iostream>
#include <string>
#include <vector>

using namespace std;

string rep[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool dfs(string &ans, int digit, vector<int> &counts)
{
    bool has_digit = true;
    for (auto c: rep[digit])
    {
        if (counts[c-'A'] < 1) {
            has_digit = false;
            break;
        }
    }
    if (!has_digit)
        return false;
    if (has_digit) {
        for (auto c: rep[digit])
        {
            counts[c-'A']-- ;
        }
    }
    ans += '0'+digit;
    bool all_used = true;
    for (int i = 0; i < 26; ++i)
        if (counts[i]) {
            all_used = false;
            break;
        }
    if (all_used) return true;
    for (int i = digit; i < 10; ++i)
        if (dfs(ans, i, counts))
            return true;

    for (auto c: rep[digit])
    {
        counts[c-'A']++ ;
    }
    ans.pop_back();

    return false;
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        string pn; cin >> pn;
        vector<int> counts(26);
        auto L = pn.size();
        for (int i = 0; i < L; ++i)
            counts[pn[i] - 'A']++;

        string ans;
        for (int i = 0; i < 10; ++i)
            if (dfs(ans, i, counts))
                break;

        cout << "Case #" << t << ": " << ans << "\n";
    }

    return 0;
}


