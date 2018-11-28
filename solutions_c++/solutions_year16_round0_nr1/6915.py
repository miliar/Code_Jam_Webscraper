#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
bool vis[13];
LL cont;
int main()
{
    int t;
    LL n , m , i;
    //freopen("hello.in" ,  "r" , stdin);
    //freopen("rreess.out" , "w" , stdout);
    scanf("%d" , &t);
    for(int ca = 1 ; ca <= t ; ca++) {
        scanf("%lld" , &n);
        printf("Case #%d: " , ca);
        if(n == 0) {
            printf("INSOMNIA\n");
        }
        else {
            memset(vis , false , sizeof(vis));
            cont = 0 , i = 0;
            while(cont < 10) {
                m = n * (++i);
                for( ; m ; m /= 10) {
                    if(!vis[m % 10]) {
                        vis[m % 10] = true;
                        cont++;
                    }
                }
            }
            printf("%lld\n" , i * n);
        }
    }
}