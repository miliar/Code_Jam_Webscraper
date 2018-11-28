#include <cstdio>
#include <algorithm>
using namespace std;

int s[10000];

int main()
{
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
        int N, X;
        scanf("%d%d", &N, &X);
        
        for(int i = 0; i < N; i++)
            scanf("%d", s + i);
        sort(s, s + N);
        int ans = 0;
        int a = 0, b = N - 1;
        while(a <= b)
            if(a == b)
            {
                ans++;
                break;
            }
            else if(s[b] + s[a] <= X)
                ans++, b--, a++;
            else
                ans++, b--;
        printf(" %d\n", ans);
    }
    return 0;
}
