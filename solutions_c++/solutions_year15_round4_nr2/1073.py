#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

struct tap {
    long double r;
    long double c;
    
    friend bool operator < (tap a, tap b) {
        return a.c < b.c;
    }
};

long double v, x;
int n;
tap taps[150];

bool canDo(long double s) {
    long double cv = 0, ct = 0;
    int i;
    for (i = 0; i < n; i++) {
        if (ct + s * taps[i].c * taps[i].r >= v*x) {
            if ((v*x - ct) + 1e-14 < (v - cv) * taps[i].c) {
                fprintf(stderr, "false1\n");
                return false;
            }
            else
                break;
        }
        cv += s * taps[i].r;
        ct += s * taps[i].r * taps[i].c;
    }
    if (i == n)
        return false;
    cv = 0;
    ct = 0;
    for (i = n-1; i >= 0; i--) {
        if (ct + s * taps[i].c * taps[i].r >= v*x) {
            if ((v*x - ct) - 1e-14 > (v - cv) * taps[i].c) {
                fprintf(stderr, "false2\n");
                return false;
            }
            else
                break;
        }
        cv += s * taps[i].r;
        ct += s * taps[i].r * taps[i].c;
    }
    if (i == -1)
        return false;
    return true;
}

long double binsearch(long double start, long double end) {
    fprintf(stderr, "binsearching %Lf %Lf\n", start, end);
    
    if (end - start < 1e-7L) 
        return (start+end)/2;
    double mid = (start+end)/2;
    if (canDo(mid))
        return binsearch(start, mid);
    return binsearch(mid, end);
}

int main() {
    int TT, T;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
                fprintf(stderr, "Case #%d: \n", T);

        scanf("%d%Lf%Lf", &n, &v, &x);
        int i;
        for (i = 0; i < n; i++)
            scanf("%Lf%Lf", &taps[i].r, &taps[i].c);
        sort(taps, taps+n);
            
            fprintf(stderr, "%d\n", n);
        if (taps[0].c > x || taps[n-1].c < x) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
           fprintf(stderr, "%d\n", n);
        
        printf("%.7Lf\n", binsearch(0.0L, 100000001.0L));
        
           fprintf(stderr, "%d\n", n);
        
        
    }
}
        