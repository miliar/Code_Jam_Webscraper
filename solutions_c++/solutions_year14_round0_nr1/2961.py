#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstdlib>
#include<sstream>
#include<string.h>
#include<set>
#include<map>
#include<assert.h>
#include<ctime>
#include<queue>
#include<vector>
#include<stack>
#include<list>
#include<math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long int lli;

#define MAXN 1000005
#define INF 2147483647
#define MOD 1000000007
#define pb push_back 
#define sz(a) int((a).size())
#define FOR(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define all(c) c.begin(),c.end()
#define mset(a,b) memset(a,b,sizeof(a))

int main()
{
	int t,r,x;
	bool A[20];
	vi ans;
	// #ifndef ONLINE_JUDGE
 //    freopen("input.txt","r",stdin);
 //    #endif
    scanf("%d",&t);
    int flag = 0;
    rep(q,t)
    {
    	ans.clear();
    	rep(i,17)
    	A[i] = false;
    	scanf("%d",&r);
    	r--;
    	rep(i,4)
    	rep(j,4)
    	{
    		scanf("%d",&x);
    		if(i==r)
    		{
    			A[x] = true;
    		}
    	}
    	scanf("%d",&r);
    	r--;
    	rep(i,4)
    	rep(j,4)
    	{
    		scanf("%d",&x);
    		if(i==r)
    		{
    			if(A[x]==true)
    				ans.pb(x);
    		}
    	}
    	if(ans.size()==1)
    		printf("Case #%d: %d\n",q+1,ans[0]);
    	else if(ans.size()>1)
    		printf("Case #%d: Bad magician!\n",q+1);
    	else if(ans.size()==0)
    		printf("Case #%d: Volunteer cheated!\n",q+1);
    }
	return 0;
}
