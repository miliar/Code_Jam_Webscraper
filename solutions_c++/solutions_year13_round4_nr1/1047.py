#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Ticket Swapping

#define MOD 1000002013LL

int main()
{
    string line;

    int cases;
    cin >> cases;

    for (int caseno = 1; caseno <= cases; caseno++) {
        int N, M;
        cin >> N >> M;
        vector <long long> ent(N, 0);
        vector <long long> exi(N, 0);
        long long sum = 0;
        for (int i = 0; i < M; i++) {
            long long o, e, n;
            cin >> o >> e >> n;
            sum = (sum + (e - o + 1) * (e - o) / 2 * n) % MOD;
            ent[o - 1] += n;
            exi[e - 1] += n;
        }
        vector <long long> pas(N, 0);
        long long sum2 = 0;
        for (int i = 0; i < N; i++) {
            pas[i] += ent[i];
            long long e = exi[i];
            for (int j = i; j >= 0; j--) {
                int n = min(pas[j], e);
                sum2 = (sum2 + (i - j + 1) * (i - j) / 2 * n) % MOD;
                pas[j] -= n;
                e -= n;
            }
        }

        long long ret = ((sum2 - sum) % MOD + MOD) % MOD;
        cout << "Case #" << caseno << ": " << ret << endl;
    }

    return 0;
}
