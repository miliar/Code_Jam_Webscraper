#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <cstdio>

using namespace std;

int gcd(int a, int b)
{
    while (1) {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);
    return a / temp * b;
}

int solve(vector<int>& M, unsigned int N) {
    int leastCommonTime = 1;
    for (auto time : M) {
        leastCommonTime = lcm(leastCommonTime, time);
    }
    int period = 0;
    for (auto time : M) {
        period += leastCommonTime / time;
    }
    N %= period;

    if (N == 0) N = period;
    if (N <= M.size()) return N;

    vector<int> remainingTime{M.cbegin(), M.cend()};

    auto i=M.size();
    while (1) {
        auto min = *min_element(remainingTime.cbegin(), remainingTime.cend());
        for (auto j=0U; j<remainingTime.size(); j++) {
            remainingTime[j] -= min;
            if (remainingTime[j] == 0) {
                remainingTime[j] = M[j];
                i++;
                if (i == N) return j+1;
            }
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (auto i=1; i<=T; i++) {
        cerr << "stderr: now in case " << i << endl;
        int B, N;
        cin >> B >> N;
        vector<int> M;
        for (auto j=0; j<B; j++) {
            int b;
            cin >> b;
            M.push_back(b);
        }

        cout << "Case #" << i << ": " << solve(M, N) << endl;
    }
}
