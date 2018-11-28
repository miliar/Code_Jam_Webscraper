/*Author : Punit Singh */
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<sstream>
using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
void precompute()
{

}
int sum[2000];
int solve(string& s)
{
    int ans=0;
    sum[0]=s[0]-'0';
    for(int i=1;i<s.size();i++)
    {
        if(s[i]!='0'&&ans+sum[i-1]<i)
        {
            ans+=(i-(sum[i-1]+ans));
            //sum[i]+=i-sum[i-1];
        }
        sum[i]+=sum[i-1]+(s[i]-'0');
    }
    return ans;
}
int main()
{
    #ifdef TEST
    freopen("A-large.in","r",stdin);
 	freopen("a-largeout.txt","w",stdout);
    #endif
    precompute();
    int t,ctr=1,x,ans=0;
    string s;
    cin>>t;
    while(ctr<=t)
    {
        cin>>x>>s;
        ans=solve(s);
        for(int i=0;i<s.size();i++)
            sum[i]=0;
        printf("Case #%d: %d\n",ctr++,ans);
    }
    return 0;
}
