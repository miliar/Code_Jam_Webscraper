#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forr(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define fornr(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forrr(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define all(x) (x).begin(), (x).end()

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        int N, K; cin >> N >> K;
        vector<double> probs(N);
        forn(i, N) {
            cin >> probs[i];
        }
        unsigned int v = (1 << K) - 1;
        double best = 0.0;
        while (v < (1 << N)) {
            vector<double> ps(K+1);
            ps[0] = 1.0;
            forn(i, N) {
                if ((1 << i)&v) {
                    double p = probs[i];
                    fornr(k, K) ps[k+1] = p * ps[k] + (1.0-p)*ps[k+1];
                    ps[0] *= (1.0-p);
                }
            }
            maxi(best, ps[K/2]);


            unsigned int t = v | (v - 1);
            v = (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(v) + 1));
        }

        cout << "Case #" << casenum << ": ";
        printf("%0.6f\n", best);
    }
    return 0;
}

