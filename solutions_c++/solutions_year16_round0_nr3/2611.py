#include<cstdio>

int main() {
    int T, cnt = 0;
    long long A = (1<<15) + 1;
    scanf("%d%d%d", &T, &T, &T);
    printf("Case #1:\n");
    while(cnt < 50) {
        if(A % 3 == 0) {
            int tmp = A;
            char buf[100] = {0};
            int idx = 15;
            int i = 3;
            while(~idx) {
                buf[idx--] = tmp%2 ? '1' : '0';
                tmp >>= 1;
            }
            for(i=3; i<=10; i++) {
                long long val = 0;
                for(int j=0; j<16; j++) {
                    val *= i;
                    val += buf[j]-'0';
                }
                if(val % (i+1))
                    break;
            }
            if(i != 11) {
                A += 2;
                continue;
            }
            printf("%s ", buf);
            puts("3 4 5 6 7 8 9 10 11");
        cnt++;
        }
        A += 2;
    }
    return 0;
}
