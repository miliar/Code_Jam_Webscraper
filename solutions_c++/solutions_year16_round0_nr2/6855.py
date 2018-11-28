#include <cstdio>
#include <cstdlib>
using namespace std;

int main(int argc, char const *argv[]) {
    freopen("B-large.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    int n;
    scanf("%d\n", &n);
    for(int i=1; i<=n; i++){
        char c;
        int state;
        scanf("%c", &c);
        state = (c == '-') ? 0 : 1;
        int count = 1;
        while(1){
            scanf("%c", &c);
            if(c == '\n') break;
            if(c == '+' && state == 0){
                state = 1;
                count++;
            }
            if(c == '-' && state == 1){
                state = 0;
                count++;
            }
        }
        if(state == 1) count--;
        printf("Case #%d: %d\n", i, count);
    }
    return 0;
}
