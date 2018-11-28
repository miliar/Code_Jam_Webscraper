#include <cstdio>
#include <cstdlib>
using namespace std;

bool isall(bool a[10]){
    for(int i=0; i<10; i++){
        if(!a[i])
            return false;
    }
    return true;
}

int main(int argc, char const *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    int T, N;
    scanf("%d", &T);
    for(int i=1; i<=T; i++){
        scanf("%d", &N);
        bool a[10] = {false};
        int n = N, t;
        for(t=1; t<1000000; t++){
            int tmp = n;
            while(tmp){
                a[tmp % 10] = true;
                tmp /= 10;
            }
            if(isall(a)) break;
            n += N;
        }
        if(t >= 1000000){
            printf("Case #%d: INSOMNIA\n", i);
        } else {
            printf("Case #%d: %d\n", i, n);
        }
    }
    return 0;
}
