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
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
       int a, b, c;
       scanf("%d%d%d", &a, &b, &c);
       printf("Case #%d:", _++);
       for(int i = 0; i < c; i++) printf(" %d", i+1);
       printf("\n");
	}

    return 0;
}
