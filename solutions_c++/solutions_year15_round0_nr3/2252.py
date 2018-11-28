#include <cstdio>
#include <cstdlib>
#include <cstring>

const int N = 10010;
const int M = 4;

int multi[M][M] = {{1, 11, 12, 13},
    {11, -1, 13, -12},
    {12, -13, -1, 11},
    {13, 12, -11, -1}};
char str[N], res[N];

int get_num(char c)
{
    switch (c) {
        case 'i' : return 11;
        case 'j' : return 12;
        case 'k' : return 13;
        default : return -1;
    }
}

int mul(int a, int b)
{
    int sign = (a > 0 && b > 0) || (a < 0 && b < 0) ? 1 : -1;
    a = abs(a);
    b = abs(b);
    if (a == 1)
        return sign * b;
    if (b == 1)
        return sign * a;
    return sign * multi[a - 10][b - 10];
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int L, X;
        scanf("%d %d", &L, &X);
        scanf("%s", str);
        res[0] = get_num(str[0]);
        bool iappear = str[0] == 'i' ? true : false;
        bool jappear = false;
        for (int i = 1; i < L * X; i++) {
            int j = i % L;
            res[i] = mul(res[i - 1], get_num(str[j]));
            if (!iappear) {
                if (res[i] == 11)
                    iappear = true;
            }
            else if (!jappear) {
                if (res[i] == 13)
                    jappear = true;
            }
        }
        if (res[L * X - 1] != -1 || !iappear || !jappear)
            printf("Case #%d: NO\n", cases);
        else
            printf("Case #%d: YES\n", cases);
    }
    return EXIT_SUCCESS;
}
