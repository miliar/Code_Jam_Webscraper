/* Dijkstra */
#include<stdio.h>
#include<iostream>
using namespace std;

typedef struct {
    int sig;
    int val;
} qtr;

int res[4][4] = {
    0, 1, 2, 3,
    1, 0, 3, 2,
    2, 3, 0, 1,
    3, 2, 1, 0
};

int signal[4][4] = {
    1,  1,  1,  1,
    1, -1,  1, -1,
    1, -1, -1,  1,
    1,  1, -1, -1
};

qtr product(qtr a, qtr b)
{
    qtr c;
    c.sig = (a.sig)*(b.sig)*signal[a.val][b.val];
    c.val = res[a.val][b.val];
    return c;
}

char str[10010];

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("out_C.txt", "w", stdout);
    int i, j, r, t, T, L;
    int ok, fi, fk, ik;
    long long int X;
    qtr a, b, c;
    char code[4] = {'1', 'i', 'j', 'k'};
    int dec[256];
    dec['1'] = 0;
    dec['i'] = 1;
    dec['j'] = 2;
    dec['k'] = 3;

    scanf("%d", &T);

    for (t = 1; t <= T; t++) {
        //scanf("%d %lld", &L, &X);
        cin >> L;
        cin >> X;

        scanf(" %s", str);
        b.sig = 1;
        b.val = 0;
        fi = fk = 0;
        ok = 0;
        for (i = 1; i <= 8; i++) {
            for (j = 0; j < L; j++) {
                a.sig = 1;
                a.val = dec[str[j]];
                b = product(b, a);
                if (b.sig == 1 && b.val == 1) {
                    fi = fi == 0? i : fi;
                }
                else if (b.sig == 1 && b.val == 3) {
                    fk = (fi > 0 && fk == 0)? i : fk;
                }
            }
            if (i == 1) {
                a.sig = 1;
                a.val = 0;
                for (r = 0; r < X%4; r++) {
                    a = product(a, b);
                }
                if (a.sig == -1 && a.val == 0) ok = 1;
                else break;
            }
        }
        if (fi <= 0 || fk <= 0 || X < fk) ok = 0;
        printf("Case #%d: %s\n", t, ok == 1? "YES" : "NO");
    }

    return 0;
}
