#include <bits/stdc++.h>
using namespace std;

int solve(const string &input) {
    auto get_rightmost_minus = [] (const string &s) {
        for (int i = (int) s.size() - 1; i >= 0; i--) {
            if (s[i] == '-') return i;
        }
        return -1;
    };

    auto flip_stack = [] (const string &s, int number) {
        string buffer = s;
        for (int i = 0; i < number; i++) {
            buffer[i] = (buffer[i] == '-' ? '+' : '-');
        }
        return buffer;
    };

    int number = 0;
    int iteration = 0;
    string pancakes = input;
    while ((number = get_rightmost_minus(pancakes)) >= 0) {
        pancakes = flip_stack(pancakes, number + 1);
        iteration = iteration + 1;
    }

    return iteration;
}

int main()
{
    //freopen("/home/gdhsnlvr/Workspace/OlmProg/urozero/out", "w", stdout);

    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        string input; cin >> input;
        int res = solve(input);
        std::cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}

