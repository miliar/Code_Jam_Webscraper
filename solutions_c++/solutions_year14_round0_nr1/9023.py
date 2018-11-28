#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int n = 4;
int main()
{
    freopen("A.in", "r", stdin);
    freopen("out.txt","w", stdout);
    int T, cot = 1;
    scanf("%d",  &T);
    while(T--)
    {
        int r;
        scanf("%d",&r);
        int a[20] = {0}, b[20] = {0};
        for(int i = 1; i <= n; ++ i) for(int j = 1; j <= n; ++ j)
        {
            int x;
            scanf("%d", &x);
            if(i == r) a[x] = 1;
        }

        scanf("%d", &r);
        for(int i = 1; i <= n; ++ i) for(int j = 1; j <= n; ++ j)
        {
            int x ;
            scanf("%d", &x);
            if(i == r) b[x] = 1;
        }
        int t = 0, ans = -1;
        for(int i = 1; i <= 16; ++ i)
        {
            if(a[i] && b[i]) t++, ans = i;
        }
        printf("Case #%d: ", cot ++);
        if(t == 1) printf("%d\n", ans);
        else if(t > 1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}







