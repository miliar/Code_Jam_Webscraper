#include <iostream>
#include <string>
using namespace std;

long long best(long long w, long long l) {
    long long RES = 0LL;
    while (w+l > 0LL) {
        if (w > 0LL) {
            w--;
            RES = RES*2LL;
            l = l/2LL + w%2LL;
            w /= 2LL;
        } else {
            l--;
            RES = RES*2LL + 1LL;
            l /= 2LL;
        }
    }
    return RES;
}

long long worst(long long w, long long l) {
    long long RES = 0LL, tmp;
    while (w+l > 0LL) {
        if (l > 0LL) {
            l--;
            RES = RES*2LL + 1LL;
            w = w/2LL + l%2LL;
            l /= 2LL;
        } else {
            w--;
            RES = RES*2LL;
            w /= 2LL;
        }
    }
    return RES;
}

int main() {
    int t, T, N;
    long long P, s, e, m, BEST, WORST;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N >> P;

        s = 0LL; e = (1LL<<N);
        while (e-s > 1) {
            m = (s+e)/2LL;
            if (best((1LL<<N)-m-1LL, m) < P) s = m;
            else e = m;
        }
        BEST = s;

        s = 0LL; e = (1LL<<N);
        while (e-s > 1) {
            m = (s+e)/2LL;
            if (worst((1LL<<N)-m-1LL, m) < P) s = m;
            else e = m;
        }
        WORST = s;

        cout << "Case #" << t << ": " << WORST << ' ' << BEST << endl;
    }    

    return 0;
}
