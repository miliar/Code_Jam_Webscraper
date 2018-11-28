#include <iostream>
#include <cstdio>
#include <vector>
#include <climits>

using namespace std;


int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        string pancakes;
        cin >> pancakes;
        int m = pancakes.size();

        vector<int> plus(m+1, INT_MAX);
        vector<int> minus(m+1, INT_MAX);

        plus[0] = minus[0] = 0;

        for (int j = 1; j <= m; ++j) {
            if (pancakes[j-1] == '+') {
                plus[j] = plus[j-1];
                minus[j] = plus[j-1]+1;
            } else {
                plus[j] = minus[j-1] + 1;
                minus[j] = minus[j-1];
            }
        }

        cout << "Case #" << i << ": " << plus[m] << endl;
    }

    return 0;
}
