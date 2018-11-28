#include <cstdio>
#include <cmath>
#include <cstdlib>

enum qv {
    l, i, j, k, ml, mi, mj, mk
};

qv lut[8][8] = 
             /* 1  i  j  k -1 -i -j -k */
    /*  1 */ {{ l, i, j, k,ml,mi,mj,mk},
    /*  i */  { i,ml, k,mj,mi, l,mk, j},
    /*  j */  { j,mk,ml, i,mj, k, l,mi},
    /*  k */  { k, j,mi,ml,mk,mj, i, l},
    /* -1 */  {ml,mi,mj,mk, l, i, j, k},
    /* -i */  {mi, l,mk, j, i,ml, k,mj},
    /* -j */  {mj, k, l,mi, j,mk,ml, i},
    /* -k */  {mk,mj, i, l, k, j,mi,ml}};

class quat
{
public:
    quat ();
    quat (char name);
    quat (qv v);
    quat operator* (quat r);
    quat operator- ();
    quat operator^ (int n);
    qv val;
};

quat::quat ()
{
    val = l;
}

quat::quat (char name)
{
    val = name - 'h';
}

quat::quat (qv v)
{
    val = v;
}

quat quat::operator* (quat r)
{
    return lut[val][r.val];
}

quat quat::operator- ()
{
    return quat((val + 4) % 8);
}

quat quat::operator^ (int n)
{
    int i;
    quat q(l);
    for (i=0; i<n; i++) {
        q = q * *this;
    }
    return q;
}

int main ()
{
    int a, b, c, d;
    int T;
    int L, X;
    char s[10001];
    bool ans;
    quat I, J, K;
    quat rem, full;

    scanf("%d\n", &T);
    for (a=0; a<T; a++) {
        scanf("%d %d\n", &L, &X);
        fgets(s, L+1, stdin);
        I.val = l;
        J.val = l;
        K.val = l;
        rem.val = l;
        full.val = l;
        for (c=0; c<L; c++) {
            full = full * quat(s[c]);
        }
        ans = true;
        for (b=0; b<4 && b<X; b++) {
            for (c=0; c<L; c++) {
                I = I * quat(s[c]);
                if (I.val == i) {
                    fprintf(stderr, "i worked at b=%d, c=%d", b, c);
                    break;
                }
            }
            if (I.val == i) {
                break;
            }
        }
        if (I.val != i) {
            fprintf(stderr, "i didn't work");
            ans = false;
        }
        c = (c+1) % L;
        if (!c) b++;
        for ( ; b<8 && b<X; b++) {
            for (c=c%L; c<L; c++) {
                J = J * quat(s[c]);
                if (J.val == j) {
                    fprintf(stderr, "j worked at b=%d, c=%d", b, c);
                    break;
                }
            }
            if (J.val == j) {
                break;
            }
        }
        if (J.val != j) {
            fprintf(stderr, "j didn't work");
            ans = false;
        }
        c = (c+1) % L;
        if (!c) b++;
        for ( ; b<12 && b<X; b++) {
            for (c=c%L; c<L; c++) {
                K = K * quat(s[c]);
                rem.val = l;
                for (d=c+1; d<L; d++) {
                    rem = rem * quat(s[d]);
                }
                rem = K * rem * (full^((X-b-1)%4));
                if (rem.val == k) {
                    fprintf(stderr, "k worked at b=%d, c=%d", b, c);
                    break;
                }
            }
            if (rem.val == k) {
                break;
            }
        }
        if (rem.val != k) {
            fprintf(stderr, "k didn't work");
            ans = false;
        }
        printf("Case #%d: %s\n", a+1, (ans ? "YES" : "NO"));
    }
    return 0;
}
