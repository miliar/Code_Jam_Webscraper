//.RandomUsername (Nikola Jovanovic)
//Google Code Jam 2015
//Qualification Round
//A

#include <bits/stdc++.h>
#define MAXN 1005
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2

using namespace std;

int n;
char s[MAXN];
int sum;
int ret;
int t;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        scanf("%d", &n);
        scanf("%s", s);
        sum = 0;
        ret = 0;
        for(int i=0; i<=n; i++)
        {
            if(sum < i)
            {
                ret += (i - sum);
                sum = i;
            }
            sum += s[i] -'0';
        }
        printf("Case #%d: %d\n", tt, ret);
    }
    return 0;
}
