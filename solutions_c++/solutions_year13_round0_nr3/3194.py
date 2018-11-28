#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool palin(long long x)
{
    char str[20];
    sprintf(str, "%lld", x);
    int len = strlen(str);
    for (int i = 0; i < len; ++i) {
        if (str[i] != str[len - i - 1])
            return false;
    }
    return true;
}

int main()
{
    int T; scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase) {
        char str1[20], str2[20], str3[20];
        long long A, B; scanf("%lld%lld", &A, &B);
        long long count = 0;
        for (int i = 1; i < 10000; ++i) {
            if (i % 10 == 0) continue;
            sprintf(str1, "%d", i);
            memcpy(str2, str1, sizeof(str1));
            reverse(str2, str2 + strlen(str2));

            memcpy(str3, str2, sizeof(str2));
            strcat(str3, str2);
            long long x; sscanf(str3, "%lld", &x);
            long long xx = x * x;
            if (A <= xx && xx <= B && palin(xx))
                ++count;

            memcpy(str3, str2, sizeof(str2));
            strcat(str3, str2 + 1);
            sscanf(str3, "%lld", &x);
            xx = x * x;
            if (A <= xx && xx <= B && palin(xx))
                ++count;
        }
        printf("Case #%d: %lld\n", testcase, count);
    }
}
