/*
* @Author: Comzyh
* @Date:   2016-04-09 21:57:17
* @Last Modified by:   Comzyh
* @Last Modified time: 2016-04-09 23:30:25
*/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int T, N, J;
bool flat;
long long pow_n[11][32];
struct Answer
{
    uint8_t digital[32];
    int divider[11];
    Answer() {}
    Answer(uint32_t num)
    {
        memset(digital, 0, sizeof(digital));
        memset(divider, -1, sizeof(divider));
        for (int i = 0; num && i < 32; i++)
        {
            digital[i] = num & 1;
            num >>= 1;
        }
    }
    long long base_r(int b)
    {
        long long n = 0;
        for (int i = 0; i < N; i++)
            n += pow_n[b][i] * digital[i];
        return n;
    }
};
vector<Answer> anss;
bool is_answer(uint32_t num, Answer &ans)
{
    Answer a(num);
    for (int b = 2; b <= 10; b++)
    {
        long long n = a.base_r(b);
        for (int i = 2; i < min(10000ll, n); i ++)
            if (n % i == 0)
            {
                a.divider[b] = i;
                break;
            }
        if (a.divider[b] == -1)
            return false;
    }
    ans = a;
    return true;
}
int main()
{
    for (int i = 2; i <= 10; i++)
    {
        pow_n[i][0] = 1;
        for (int j = 1; j < 32; j ++ )
            pow_n[i][j] = pow_n[i][j - 1] * i;
    }
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        scanf("%d%d", &N, &J);
        flat = false;
        if (N > 16)
        {
            N = N / 2;
            flat = true;
        }
        anss.clear();
        for (int i = 0; i < (1 << (N - 2)); i ++)
        {
            if (anss.size() >= J)
                continue;
            Answer ans;
            if (is_answer((1 << (N - 1)) + (i << 1) + 1, ans))
                anss.push_back(ans);
        }
        printf("Case #%d:\n", TT);
        for (int i = 0; i < J; i++)
        {
            for (int k = 0; k < (flat ? 2 : 1); k ++)
                for (int j = N - 1; j >= 0; j--)
                    printf("%d", anss[i].digital[j]);
            for (int j = 2; j <= 10; j++)
                printf(" %d", anss[i].divider[j]);
            // for (int j = 2; j <= 10; j++)
            //     printf("(%lld / %d = %lf)",anss[i].base_r(j), anss[i].divider[j], double(anss[i].base_r(j)) / anss[i].divider[j]);
            printf("\n");
        }
    }
    return 0;
}