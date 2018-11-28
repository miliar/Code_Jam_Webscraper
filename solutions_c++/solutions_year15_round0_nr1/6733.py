#include <cstdio>

main(){

int casos, sum, n, res;
char buf[1024];

scanf("%d", &casos);
for(int c=1; c <= casos; c++){
    scanf("%d %s", &n, buf);
    sum = res = 0;
    for(int i=0;i<=n;i++){
        sum += (buf[i] - '0');
        if( sum <= i ){
            res++;
            sum++;
        }
    }
    printf("Case #%d: %d\n", c, res);
}

return 0;
}
