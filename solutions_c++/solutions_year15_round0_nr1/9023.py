
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int T;
    cin >> T;

    for (auto i = 0; i < T; i++) {
        int s_max;
        string line;
        cin >> s_max >> line;

        if (s_max == 0) {
            cout << "Case #" << (i + 1) << ": " <<  0 << endl;
            continue;
        }

        vector<int> audience(s_max + 1), partial_sums(s_max + 1), x(s_max);
        for (auto i = 0; i <= s_max; i++) {
            audience[i] = ((int)(line[i] - '0'));
            partial_sums[i] = audience[i] + ((i > 0)? partial_sums[i - 1] : 0);
            if (i > 0) {
                x[i - 1] = i - partial_sums[i - 1];
                //cerr << i - 1 << " " << x[i - 1] << endl;
            }
        }
 
        int answer = *max_element(x.begin(), x.end());
        answer = (answer < 0)? 0 : answer;
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
}
