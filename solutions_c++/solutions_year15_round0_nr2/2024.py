#include <cstdio>

int caculate(int highest, int* list, int num)
{
    int ans = 0;
    for (int i = 0; i < num; i++) {
        if (list[i] > highest) {
            ans += (list[i]%highest != 0);
            ans += list[i]/highest -1;
        }
    }
    return ans+highest;
}
int main(int argc, char const* argv[])
{
    int run;
    scanf("%d", &run);
    for (int times=1; times <= run; ++times) {
        int num_pencake, pencake[1001];
        scanf("%d", &num_pencake);
        int max=0;
        for (int i = 0; i < num_pencake; i++) {
            scanf("%d", pencake+i);
            if( pencake[i] > max )
                max = pencake[i];
        }
        int min_ans=0x7fffffff;
        for (int i = 1; i <= max; i++) {
            int tmp=0;
            tmp = caculate(i, pencake, num_pencake);
            if (tmp < min_ans) {
                min_ans = tmp;
            }
        }
        printf("Case #%d: %d\n", times, min_ans);
    }
    return 0;
}
