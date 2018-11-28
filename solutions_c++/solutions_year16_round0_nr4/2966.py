#include <stdio.h>
#include <string.h>
#include <algorithm>

int main()
{
#ifdef LOCAL
    freopen("/Users/yew1eb/ClionProjects/CppGo/in.txt", "r", stdin);
    freopen("/Users/yew1eb/ClionProjects/CppGo/out.txt", "w", stdout);
#endif
    int T, K, C, S;
    scanf("%d", &T);
    for(int cas=1; cas<=T; ++cas) {
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d: ", cas);
        for(int i=1; i<=S; ++i) {
            printf("%d", i);
            if(i<S) printf(" ");
            else printf("\n");
        }
    }
    return 0;
}
