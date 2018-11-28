#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <deque>

using namespace std;

int n, T, m[20];

int main () {
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	scanf ("%d", &T);
	for (int c = 1; c <= T; c++) {
        bool f = false;
        int res = 0, in;
        memset(m, 0, sizeof(m));
        scanf ("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf ("%d", &in);
                if (i == n) m[in]++;
            }
        }
        scanf ("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf ("%d", &in);
                if (i == n) m[in]++;
            }
        }
        for (int i = 1; i <= 16; i++) {
            if (m[i] == 2) {
                if (res > 0) f = true;
                res = i;
            }
        }
        printf ("Case #%d: ", c);
        if (!f) {
            if (res == 0) printf ("Volunteer cheated!\n"); else printf ("%d\n", res);
        } else printf ("Bad magician!\n");
	}
	return 0;
}
