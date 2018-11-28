#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;

long double table[203][103];

long double calc(vector<long double> &final) {
    table[0][0] = 1;
    for (int i = 1; i <= K; i ++) {
        table[i][0] = table[i-1][0] * (1.0 - final[i]);

        for (int j = 1; j <= i; j ++) {
            table[i][j] = table[i-1][j] * (1.0 - final[i]) +
                table[i-1][j-1] * final[i];
        }
    }
    return table[K][K/2];
}

int main() {
    int T;
    scanf( "%d", &T );
    for (int test = 1; test <= T; test ++) {
        scanf( "%d %d", &N, &K );

        vector<long double> data;
        for (int i = 0; i < N; i ++) {
            long double a;
            scanf( "%Lf", &a );
            data.push_back(a);
        }

        sort (data.begin(), data.end());

        vector<long double> final;
        final.push_back(0);
        for (int i = 0; i < K; i ++) {
            final.push_back(data[i]);
        }
        long double result = calc(final);
        for (int i = 0; i < K; i ++) {
            final[K - i] = data[N - i - 1];
            result = max(result, calc(final));
        }

        printf( "Case #%d: %.10Lf\n", test, result);
    }

    return 0;
}
