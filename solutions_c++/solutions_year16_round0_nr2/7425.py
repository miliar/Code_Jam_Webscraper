#include <string>
#include <algorithm>
#include <iostream>

using namespace std;


int solve(string cake) {
    cake += '+';

    int cnt = 0;

    for (int i = 1; i < cake.size(); ++i) {
        if (cake[i-1] != cake[i])
            cnt++;
    }

    return cnt;
}


int main() {
    int T;
    cin >> T;

    for (int k = 1; k <= T; ++k) {
        string cake;
        cin >> cake;

        printf("Case #%d: %d\n", k, solve(cake));
    }

    return 0;
}
