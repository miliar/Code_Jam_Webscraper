# include<algorithm>
# include<stdlib.h>
# include<iostream>
# include<string.h>
# include<cstring>
# include<cstdlib>
# include<stdio.h>
# include<ctype.h>
# include<time.h>
# include<math.h>
# include<vector>
# include<cstdio>
# include<bitset>
# include<string>
# include<cctype>
# include<queue>
# include<stack>
# include<deque>
# include<cmath>
# include<map>
# include<set>
# define dist(x,y,xx,yy) sqrt( ((x-xx)*(x-xx)+(y-yy)*(y-yy))*1.0 )
# define pf push_front
# define pb push_back
# define mp make_pair
# define pr printf
# define se second
# define si size()
# define sc scanf
# define fi first
# define er erase
# define be begin
# define ss size
# define Int long long int
# define eps 0.00000001
# define INF 1000000007
# define MOD 1000000007
# define MN 100005
using namespace std;
int t,n,i,j,k,c,d;
char s[MN];
main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    #endif
    sc("%d",&t);
    for(k=1;k<=t;k++)
    {
        sc("%d%s",&n,s);
        d=c=0;
        for(i=0;i<=n;i++)
        {
            if(s[i]!='0' && d<i)c+=i-d,d=i;
            d+=s[i]-48;
        }
        pr("Case #%d: %d\n",k,c);
    }
    return 0;
}
