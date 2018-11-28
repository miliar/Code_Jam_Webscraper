#include <cstdio>

int main(int argc, char const* argv[])
{
    int run;
    scanf("%d", &run);
    for (int times=1; times <= run; ++times) {
        int num=0, zzz=0, now_stand=0; 
        bool audience[10]={0};
        scanf("%d", &num);
        getchar();
        for (int i = 0; i <= num; i++) {
            char c = getchar();
            int tmp = c - '0';
            if (now_stand < i) {
                zzz += i - now_stand;
                now_stand = i;
            }
            now_stand += tmp;
        }
        printf("Case #%d: %d\n", times, zzz);

    }
    return 0;
}
