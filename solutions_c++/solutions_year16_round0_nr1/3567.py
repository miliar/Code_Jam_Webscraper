#include <stdio.h>
#include <string.h>
#include <algorithm>

int solve(int n);

int add(int tmp);

void bprint(unsigned int code);

using namespace std;

int main()
{
#ifdef LOCAL
    freopen("/Users/yew1eb/Downloads/A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int T, N;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &N);
        printf("Case #%d: ", cas);
        if(N==0) puts("INSOMNIA");
        else {
            printf("%d\n", solve(N));
        }
    }
    return 0;
}

unsigned int overValue = (1<<10) - 1;
unsigned int limit = (1<<32) - 1;

int solve(int n) {
    int tmp = 0;
    unsigned int hashCode = 0;
    do {
        tmp += n;
        hashCode |= add(tmp);
        //bprint(hashCode);puts("");
        if(hashCode == overValue) {
            return tmp;
        }
    } while( tmp < limit - n);
    return tmp;
}

void bprint(unsigned int code) {
    if(code>>1) bprint(code>>1);
    printf("%d", code&1);
}

int add(int tmp) {
    int ret = 0;
    while(tmp > 0) {
        short x = tmp % 10;
        ret |= (1<<x);
        tmp /= 10;
    }
    return ret;
}