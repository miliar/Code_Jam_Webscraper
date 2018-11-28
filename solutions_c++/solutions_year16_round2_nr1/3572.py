#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// todo stop using globals
vector<int> sol;

bool rec(int left, const vector<int>& path, const unordered_map<char, int>& letters,
         const vector<string>& digits
) {
    if (left == 0)
    {
        sol = path;
        return true;
    }

    // try each letter
    int start = 0;
    if (path.size() > 0)
        start = path.back();
    for (int i = start; i <= 9; i ++)
    {
        string d = digits[i];

        if (d.size() <= left)
        {
            // check we have enough letters for this number
            unordered_map<char, int> new_letters(letters);
            bool valid_digit = true;
            for (int j = 0; j < d.size(); j ++)
            {
                if (new_letters[d[j]] >= 1)
                {
                    new_letters[d[j]] --;
                }
                else
                {
                    valid_digit = false;
                    break;
                }
            }

            if (valid_digit)
            {
                vector<int> new_path(path);
                new_path.push_back(i);
                if (rec(left - d.size(), new_path, new_letters, digits))
                    return true;
            }
        }

    }

    return false;
}

void solve(int test_nr)
{
    string s;
    cin >> s;

    // Count the number of occurrences of each letter
    unordered_map<char,int> letters;
    for (int i = 0; i < s.length(); i ++)
    {
        letters[s[i]] ++;
    }

    vector<string> digits {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
                           "SIX", "SEVEN", "EIGHT", "NINE"};
    // Go through the digits in increasing order and try to find a match
    cout << "Case #" << test_nr << ": ";
    if (rec(s.length(), vector<int>(), letters, digits))
    {
        for (int i = 0; i < sol.size(); i ++)
        {
            cout << sol[i];
        }
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
