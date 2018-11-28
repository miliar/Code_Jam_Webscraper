
#include <bits/stdc++.h>
using namespace std;

#define EPS 1e-10

struct Hiker {
    int initial, speed;
    Hiker(int i, int s) : initial(i), speed(s) { }
    Hiker() { }

    inline double P() const { return initial * M_PI / 180; }
    inline double S() const { return 2 * M_PI / speed; }

    double position(double t) const {
        return P() + S() * t;
    }
    double reach() const {
        return (2 * M_PI - P()) / S();
    }
    int encounters(double t) const {
        double x = position(t);
        if (x <= 2 * M_PI) return 1;
        return (x / (2 * M_PI)) - 1;
    }
};
struct Group : public Hiker {
    int count;
    Group(int i, int s, int c) : Hiker(i, s), count(c) { }
    Group() { }
};

int solve(const vector<Hiker> &H) {
    int mval = -1, n = H.size(), i, j;
    for (i = 0; i < n; i++) {
        int enc = 0;
        double time = H[i].reach();
        for (j = 0; j < n; j++)
            if (j != i)
                enc += H[j].encounters(time);
        if (enc < mval || mval < 0)
            mval = enc;
    }
    return mval;
}

main() {
    int T, N, i, j, k;
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> N;
        vector<Group> G(N);
        vector<Hiker> H;
        for (j = 0; j < N; j++) {
            cin >> G[j].initial >> G[j].count >> G[j].speed;
            for (k = 0; k < G[j].count; k++)
                H.push_back(Hiker(G[j].initial, G[j].speed + k));
        }
        int res = solve(H);
        cout << "Case #" << (i + 1) << ": " << res << endl;
    }
}
