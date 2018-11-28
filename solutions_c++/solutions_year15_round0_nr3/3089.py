#include <stdio.h>

int T;
long long X, L;
long long real_L;
int S[100000];
int memo[100000];
int calc_value(int a, int b);
bool find_answer(long long idx, int what);

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    FILE *out = fopen("Output.txt", "w");
    int T;
    scanf("%d", &T);

    for(int loop = 1; loop <= T; loop++)
    {
        for(int i = 0; i < 100000; i++) memo[i] = 0;
        scanf("%lld %lld", &L, &X);

        for(int i = 1; i <= L; i++)
        {
            char c;
            scanf("%c", &c);
            while(c <= 'g') scanf("%c", &c);
            S[i] = c - 'g'; // i = 2, j = 3; k = 4;
        }

        real_L = L * X;
        bool ans = (real_L >= 3) ? find_answer(1, 2) : false;
        if(ans == true)
        {
            printf("Case #%d: YES\n", loop);
            fprintf(out, "Case #%d: YES\n", loop);
        }
        else
        {
            printf("Case #%d: NO\n", loop);
            fprintf(out, "Case #%d: NO\n", loop);
        }
    }
}

int calc_value(int a, int b)
{
    // 1 = 1, i = 2, j = 3, k = 4;
    int result = (a*b > 0) ? 1 : -1;
    a = (a>0) ? a : -a;
    b = (b>0) ? b : -b;

    int result_table[5][5] =
    {
        { 0, 0, 0, 0, 0 },
        { 0, 1, 2, 3, 4 },
        { 0, 2, -1, 4, -3 },
        { 0, 3, -4, -1, 2 },
        { 0, 4, 3, -2, -1 }
    };
    result *= result_table[a][b];
    return result;
}

bool find_answer(long long idx, int what)
{
    int now_val = 1;
    for(long long i = idx; i <= real_L; i++)
    {
        int real_idx = i % L;
        if(real_idx == 0) real_idx = L;

        if(what == 4 && memo[i] != 0)
        {
            now_val = calc_value(now_val, memo[i]);
            break;
        }

        now_val = calc_value(now_val, S[real_idx]);
        if(what == now_val && (what == 2 || what == 3)) // what = i, j
        {
            bool res = find_answer(i+1, what+1);
            if(res == true) return true;
        }
    }
    if(what == 4) memo[idx] = now_val;
    if(what == 4 && now_val == 4) return true;
    return false;
}
