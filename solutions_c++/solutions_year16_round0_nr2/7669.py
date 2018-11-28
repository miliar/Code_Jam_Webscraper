#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <set>
#include <cstdlib>
#include <vector>

using namespace std;

bool is_ready(string &s)
{
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            return false;
        }
    }

    return true;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        string s;
        cin >> s;

        long long steps = 0;

        while (!is_ready(s)) {
            steps++;
            string new_s;
            int j;
            for (j = s.size() - 1; j >= 0; --j) {
                if (s[j] == '-') { // last -
                    break;
                }
            }

            int counter = 0;
            for (int k = 0; k < j; ++k) {
                if (s[k] == '-') {
                    counter++;
                }
            }
            if (counter == j) {
                for (int t = 0; t <= j; ++t) {
                    s[t] = '+';
                }
            }
            else {
                if (s[0] != '-') {
                    int k = 0;
                    while (s[k] == '+') {
                        s[k] = '-';
                        k++;
                    }
                    steps++;
                }

                for (int k = j; k >= 0; --k) {
                    if (s[k] == '+') {
                        new_s.push_back('-');
                    }
                    else {
                        new_s.push_back('+');
                    }
                }

                for (int k = j + 1; k < s.size(); ++k) {
                    new_s.push_back(s[k]);
                }

                s = new_s;
            }
        }

        cout << "Case #" << i << ": " << steps << endl;
    }

    return 0;
}
