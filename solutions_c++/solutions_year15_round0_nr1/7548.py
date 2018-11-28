#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;

void solve()
{
    int n, s, ans;
    char c;

    scanf("%d ", &n);
    n++;
    s = ans = 0;
    for(int i = 0; i <= n; i++)
    {
        scanf("%c", &c);
        c = c - '0';
        if(c > 0 && s < i)
        {
            ans += (i - s);
            s += (i - s);
        }
        s += c;
    }
    printf("%d\n", ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int cases;
    scanf("%d\n", &cases);

    for(int i = 1; i <= cases; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
	return 0;

}
