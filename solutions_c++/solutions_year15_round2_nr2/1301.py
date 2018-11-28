#include <bits/stdc++.h>
using namespace std;

int R, C;
int N;

int getbit(int r, int c)
{
    return 1<<(r*C+c);
}
int get(int n, int rem, int state)
{
    if (N-n < rem) {
        return 100;
    }
    if (n >= N) {
        return 0;
    }
    int r = n/C;
    int c = n%C;
    int bit = getbit(r,c);
    // emtpy
    int ret = get(n+1, rem, state);
    // stay;
    if (rem) {
        int ns = state|bit;
        int ct = 0;
        if (r > 0) {
            int t = getbit(r-1, c);
            if (state&t) {
                ++ct;
            }
        }
        if (c > 0) {
            int t = getbit(r, c-1);
            if (state & t) {
                ++ct;
            }
        }
        ret = min(ret, ct + get(n+1, rem-1, ns));
    }
    return ret;
}
int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> R >> C >> N;
        printf("Case #%d: %d\n", i, get(0,N,0));
    }
}
