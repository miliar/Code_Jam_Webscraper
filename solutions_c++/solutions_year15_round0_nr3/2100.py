#include <cstdio>
int table[4][4] = {
    {1,2,3,4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}
};
int string[100001];
int prefix[100001];
int length, repeat;
int compute(int a, int b) {
    int tmpA = (a>0)? a : -a;
    int tmpB = (b>0)? b : -b;
    return table[tmpA-1][tmpB-1] * (((a > 0) != (b > 0))? -1 : 1);
}

bool search(int length)
{
    bool find = false;
    for (int i = 0; i <= length; i++) {
        if (prefix[i] == 2)
            find = true;
        if (prefix[i] == 4 && find)
            return true;
    }
    return false;
}

int main(int argc, char const* argv[])
{
    int run;
    scanf("%d", &run);
    for (int times=1; times <= run; ++times) {
        char input[10001];
        scanf("%d%d%s", &length, &repeat, input);
        for (int i = 0; i < length; i++) {
            string[i] = input[i] - 'i' + 2;
            for (int j = 1, l=i+length; j < repeat; j++, l+=length) {
                string[l] = string[i];
            }
        }
        int total_len = length*repeat;
        prefix[0] = 1;
        for (int i = 1; i <= total_len; i++) {
            prefix[i] = compute(prefix[i-1], string[i-1]);
        }
        bool ans = false;
        if (prefix[total_len] == -1)
            ans = search(repeat*length);
        printf("Case #%d: %s\n", times, ans ? "YES" : "NO");
    }
    return 0;
}
