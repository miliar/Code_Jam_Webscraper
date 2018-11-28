#include <cstdio>
#include <bitset>

const int N = 10;

std :: bitset<N> f;

int main () {
        #ifndef FILE_STREAM
        	#define fname "aa"
                freopen (fname".in", "r", stdin);
                freopen (fname".out", "w", stdout);
        #endif // FILE_STREAM
        int n; scanf ("%d\n", &n);
        for (int test = 1; test <= n; test++) {
                int x; scanf ("%d\n", &x);
                int t = x;
                int cnt = 0;
                for (int i = 1; i <= 100; i++, x += t) {
                        int tx = x;
                        while (tx > 0) cnt += f[tx % 10] == 0, f[tx % 10] = 1, tx /= 10;
                        if (cnt == 10) break;
                }
                f.reset ();
                printf ("Case #%d: ", test);
                if (cnt == 10) printf ("%d\n", x);
                else puts ("INSOMNIA");
        }
        return 0;
}
