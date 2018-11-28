#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int c[20], cc;

void count(int x) {
    while(x > 0) {
        if(c[x % 10] == 0) {c[x % 10] = 1; cc++; }
        x /= 10;
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
        memset(c,0,sizeof(c));
        cc = 0;
        int n;
        scanf("%d", &n);
	    printf("Case #%d: ", _++);
        if(n == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        int now = n;
        while(1) {
            count(now);
            if(cc == 10) break;
            now += n;
        }
        printf("%d\n", now);
	}

    return 0;
}
