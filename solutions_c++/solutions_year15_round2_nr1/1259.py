/*

    Harsh Vardhan :)

*/

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<stack>

using namespace std;

#define MAX 1111111
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define tr(v, it) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define mp make_pair
#define F first
#define S second
#define SET(p,v) memset(p, v, sizeof(p))
#define chkC(x,n) (x[n>>6]&(1<<((n>>1)&31)))
#define setC(x,n) (x[n>>6]|=(1<<((n>>1)&31)))
typedef long long ll;
typedef pair<int,int> pii;

int dp[MAX];
queue<int> Q;
int solve(int x)
{
	int r = 0;
	while (x > 0)
	{
		r = r * 10 + (x % 10);
		x /= 10;
	}
	return r;
}

int main()
{
    //freopen("H:\\input.txt","r",stdin);
    //freopen("H:\\output.txt","w",stdout);
    dp[1] = 1;
    Q.push(1);
    while (!Q.empty())
    {
        int x = Q.front();
        Q.pop();
        if (x + 1 < MAX and dp[x + 1] == 0)
        {
            dp[x + 1] = dp[x] + 1;
            Q.push(x + 1);
        }
        if (solve(x) < MAX and dp[solve(x)] == 0)
        {
            dp[solve(x)] = dp[x] + 1;
            Q.push(solve(x));
        }
    }
    int t;
    gi(t);
    for(int i=1;i<=t;i++)
    {
        int n;
        gi(n);
        printf("Case #%d: %d\n",i, dp[n]);

    }

   return 0;
}