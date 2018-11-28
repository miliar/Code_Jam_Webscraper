#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        long long num;
        cin >> num;

        if (num == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        set<int> diff_nums;
        long long current_num = 0;
        do {
            current_num += num;
            stringstream ss;
            ss << current_num;
            string num_str = ss.str();
            for (int j = 0; j < num_str.size(); ++j) {
                int digit = num_str[j];
                diff_nums.insert(digit);
            }
        }
        while (diff_nums.size() < 10);

        cout << "Case #" << i << ": " << current_num << endl;
    }

    return 0;
}
