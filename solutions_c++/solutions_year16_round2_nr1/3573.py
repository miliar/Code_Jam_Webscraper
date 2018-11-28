#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

string digit[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
        "SEVEN", "EIGHT", "NINE"};

string findNum(string S)
{
    for (int i = 0; i <= 9; ++i) {
        string d = digit[i];

        if (S.size() < d.size()) {
            continue;
        }

        string s = S;
        int j;
        for (j = 0; j < d.size(); ++j) {
            int k = s.find_first_of(d[j]);
            if (k != string::npos) {
                s.erase(k, 1);
            }
            else {
                break;
            }
        }

        if (j == d.size()) {
            if (s.size() == 0) {
                return to_string(i);
            }

            string ans = findNum(s);
            if (ans != "DUMMY") {
                return to_string(i) + ans;
            }
        }
    }

    return "DUMMY";
}

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;



    for (t = 1; t <= T; ++t) {
        string ans;
        string S;
        cin >> S;

        ans = findNum(S);

        cout << "Case #" << t << ": " << ans  << endl;
    }

    return 0;
}
