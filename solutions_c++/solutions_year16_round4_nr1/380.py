#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int n, r, p, s;

bool step(int cnt[3], string cd[3], int ncnt[3], string ncd[3]) {
    int s = cnt[0] - cnt[1] + cnt[2];
    if (s % 2 == 1) {
        return false;
    }
    ncnt[1] = s / 2;
    ncnt[0] = cnt[0] - ncnt[1];
    ncnt[2] = cnt[2] - ncnt[1];
    if (ncnt[0] < 0 || ncnt[1] < 0 || ncnt[2] < 0) {
        return false;
    }
    ncd[0] = cd[0] + cd[1];
    ncd[1] = cd[0] + cd[2];
    ncd[2] = cd[1] + cd[2];
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d %d %d", &n, &r, &p, &s);
        string cd[3];
        int cn[3];
        cn[0] = p;
        cn[1] = r;
        cn[2] = s;
        cd[0] = "P";
        cd[1] = "R";
        cd[2] = "S";
        while (n > 0) {
            string ncd[3];
            int ncn[3];
            if (!step(cn, cd, ncn, ncd)) {
                printf("Case #%d: IMPOSSIBLE\n", t);
                cn[0] = cn[1] = cn[2] = -1;
                break;
            }
            --n;
            for (int i = 0; i < 3; ++i) {
                cd[i] = ncd[i];
                cn[i] = ncn[i];
            }
        }
        for (int i = 0; i < 3; ++i) {
            if (cn[i] == 1) {
                printf("Case #%d: %s\n", t, cd[i].c_str());
            }
        }
    }
    return 0;
}
