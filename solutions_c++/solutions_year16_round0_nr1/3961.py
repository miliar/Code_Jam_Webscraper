#include <cstdio>
#include <cstring>

int T, n;
bool v[10];
char s[20];

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        scanf("%d", &n);
        printf("Case #%d: ", i);
        if (n == 0) printf("INSOMNIA\n");
        else{
            int c = 0, ct = 0;
            memset(v, 0, sizeof(v));
            while (ct < 10){
                int len;
                c += n;
                sprintf(s, "%d", c);
                len = strlen(s);
                for (int j = 0; j < len; j++){
                    if (!v[s[j] - '0']) v[s[j] - '0'] = true, ct++;
                }
            }
            printf("%d\n", c);
        }
    }
}
