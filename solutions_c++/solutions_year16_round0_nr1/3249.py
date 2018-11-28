#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
int vis[10];
int main(void)
{
    int T;
    scanf("%d", &T);
    int g = 0, n;
    while(T--){
        printf("Case #%d: ", ++g);
        scanf("%d", &n);
        if (n == 0){
            puts("INSOMNIA");
            continue;
        }
        memset(vis, 0, sizeof(vis));
        int num = 10;
        bool flag = 0;
        for(int i = 1; i <= 100; ++ i){
            int x = n * i;
            while(x != 0){
                if(vis[x % 10] == 0){
                    vis[x % 10] = 1;
                    num --;
                }
                x /= 10;
            }
            if (num == 0){
                flag = 1;
                printf("%d\n", i * n);
                break;
            }
        }
        if(!flag){
            puts("INSOMNIA");
        }
    }
    return 0;
}