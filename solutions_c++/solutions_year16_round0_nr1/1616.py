#include <bits/stdc++.h>

using namespace std;

int main (void) {
    int T;
    scanf ("%d", &T);
    for (int c = 1; c <= T; ++c) {
        long long int N;
        cin >> N;
        printf ("Case #%d: ", c);
        if (N == 0) printf ("INSOMNIA\n");
        else {
            set <int> S;
            long long int K = N;
            while (S.size() != 10) {
                long long int C = K;
                while (C > 0) S.insert (C%10), C /= 10;
                if (S.size() != 10) K += N;
            }
            printf ("%lld\n", K);
        }
    }
}
