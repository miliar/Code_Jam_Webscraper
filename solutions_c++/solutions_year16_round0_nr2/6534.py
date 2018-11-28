#include <cstdio>
#include <cstring>
using namespace std;

char str[10000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++ i)
    {
        scanf("%s", &str);
        int l = strlen(str);
        int x = 0;
        int ans = 0;
        for (int j = l - 1; j >= 0; -- j)
        {
            int k = str[j] == '+' ? 1 : 0;
            if ((k ^ x) == 0) 
            {
                ++ ans;
                x ^= 1;
            }
        }
        
        printf("Case #%d: %d\n", i, ans);
    }
}
                