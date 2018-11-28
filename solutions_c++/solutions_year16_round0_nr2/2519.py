#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;
using namespace std;

int recursive(char *in, int pt)
{
    if (pt == 0)
    {
        if (in[0] == '+') return 0;
        else return 1;
    }
    if (in[pt] == '+') return recursive(in, pt-1);
    else
    {
        for (int i = 0; i <= pt; i++)
        {
            if (in[i] == '+') in[i] = '-';
            else in[i] = '+';
        }
        return 1 + recursive(in, pt - 1);
    }
}

void solve()
{
    char in[1000];
    int ans = 0;

    scanf("%s", in);

    ans = recursive(in, strlen(in)-1);

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
