#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

char s[100010];

int getv(char c) {
    if(c == 'a' || c == 'i' || c == 'o' || c == 'u' || c == 'e') return 0;
    return 1;
}

int f[1000010];

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        int x, y;
        scanf("%d%d", &x, &y);
        printf("Case #%d: ", cnt++);
        if(x > 0) {
            for(int i = 0; i < x; i++) printf("WE");
        } else for(int i = 0; i < -x; i++) printf("EW");

        if(y > 0) {
            for(int i = 0; i < y; i++) printf("SN");
        } else for(int i = 0; i < -y; i++) printf("NS");

        puts("");
    }

    return 0;
}
