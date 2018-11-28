#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
#include <string>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    int T;
    cin >> T;

    vector<string> input;
    input.reserve(T);
    copy_n(istream_iterator<string>(cin), T, back_inserter(input));

    for (int i = 0; i < T; ++i) {
        int num_flip = 0;
        string& curr_str = input[i];
        while (true) {
            char t = curr_str[0];
            int j = 1;
            while (j < curr_str.length() && curr_str[j] == t) {
                ++j;
            }
            if (j == curr_str.length() && t == '+')
                break;
            t = t == '+' ? '-' : '+';
            fill(curr_str.begin(), next(curr_str.begin(), j), t);
            ++num_flip;
        }

        cout << "Case #" << (i+1) << ": " << num_flip << "\n";
    }
    return 0;
}