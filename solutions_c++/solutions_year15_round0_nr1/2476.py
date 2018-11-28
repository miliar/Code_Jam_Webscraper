#include <cstdio>
using namespace std;

void solve(int t)
{
    int n;
    scanf("%d",&n);
    char s[1010];
    scanf("%s",s);

    int num = s[0]-'0';
    int sol = 0;
    for(int i = 1; i <= n; i++)
    {
        if (s[i] == '0')
            continue;
        if ( i > num)
        {
            sol += i - num;
            num = i;
        }
        num += s[i]-'0';
    }
    printf("Case #%d: %d\n",t,sol);
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
        solve(i);
    return 0;
}
