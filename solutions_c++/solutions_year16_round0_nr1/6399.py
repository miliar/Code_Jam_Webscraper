#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
#include <c++/algorithm>

using namespace std;

long long last_num(int N)
{
    if (N == 0) return 0;
    int num_found = 0;
    bool found[10] = {false};
    long long curr_N = N;
    while (true) {
        long long t = curr_N;
        while (t) {
            if (!found[t%10]) {
                found[t%10] = true;
                ++num_found;
            }
            t /= 10;
        }
        if (num_found == 10) break;
        curr_N += N;
    }
    return curr_N;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    vector<int> input;
    input.reserve(T);
    copy_n(istream_iterator<int>(cin), T, back_inserter(input));
    for (int i = 0; i < input.size(); ++i) {
        long long t = last_num(input[i]);
        cout <<"Case #" << i+1 << ": ";
        if (t == 0) {
            cout << "INSOMNIA";
        } else {
            cout << t;
        }
        cout << "\n";
    }
    return 0;
}