#include <stdio.h>
#include <string.h>

#define I       (2)
#define J       (3)
#define K       (4)

int mult(int a, int b)
{
    static int mtx [5][5] =
    {
    /*0*/{ 0, 0, 0, 0, 0},
    /*1*/{ 0, 1, I, J, K},
    /*I*/{ 0, I,-1, K,-J},
    /*J*/{ 0, J,-K,-1, I},
    /*K*/{ 0, K, J,-I,-1}
    };
    int sign = 1;
    if (a < 0) {
        a *= -1;
        sign *= -1;
    }
    if (b < 0) {
        b *= -1;
        sign *= -1;
    }
    return mtx[a][b] * sign;
}

int inverse(int a, int b)
{
    static int mtx [5][5] =
    {
    /*0*/{ 0, 0, 0, 0, 0},
    /*1*/{ 0, 1,-I,-J,-K},
    /*I*/{ 0, I, 1, K,-J},
    /*J*/{ 0, J,-K, 1, I},
    /*K*/{ 0, K, J,-I, 1}
    };
    int sign = 1;
    if (a < 0) {
        a *= -1;
        sign *= -1;
    }
    if (b < 0) {
        b *= -1;
        sign *= -1;
    }
    return mtx[a][b] * sign;
}

int char2val(char c)
{
    switch (c) {
    case 'i':
        return I;
    case 'j':
        return J;
    case 'k':
        return K;
    }
    return 0;
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        static long long L, X;
        static char buffer [10002];
        static char fullbuffer [10002];
        scanf("%lld %lld %s", &L, &X, fullbuffer);
        char * nail = fullbuffer + L;
        for (int x = 1; x < X;) {
            int toCopy = x;
            if (X - x < x) {
                toCopy = X - x;
            }
            memcpy(nail, fullbuffer, toCopy * L);
            nail += L * toCopy;
            x += toCopy;
        }
        *nail = '\0';
        int vL [10002];
        bool mem [5][5];
        int len = X * L;
        vL[0] = 1;
        for (int i = 1; i <= len; i++) {
            vL[i] = mult(vL[i - 1], char2val(fullbuffer[i - 1]));
        }
        bool canDo = false;
        for (int i = 1; !canDo && i < len; i++) {
            for (int j = i + 1; !canDo && j < len; j++) {
                int left = vL[i];
                int right = inverse(vL[len], vL[j]);
                int middle = inverse(vL[j], left); 
                if (middle == J && left == I && right == K) 
                    canDo = true;
            }
        }
        printf("Case #%d: %s\n", t, canDo ? "YES" : "NO");
    }
}
