#include<iostream>
#include<stdio.h> 
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<stack>
#include<assert.h>
#include<limits.h>
#define tr(i) for(typeof(i.begin()) it=i.begin(); it!=i.end();it++)
#define pb push_back
#define mp make_pair
#define REP(i,n) for(int i=0;i<n;i++)
#define rep(i,s,n) for(int i=s;i<n;i++)
#define s(n) scanf("%d",&n)
#define XX first
#define X first
#define Y second
#define all(a) a.begin(),a.end()
#define YY second.first
#define ZZ second.second
#define fill(a,b) memset(a,b,sizeof(a))
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end());
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define SZ(x) (int)(x.size())
#define lin(val,j) (DP[j]-val*D[j])
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
#define MN 4

bool poss[16];
int grid[MN][MN];

int main()
{	
	int T; s(T);
	int a;
	REP(cc,T)
	{
		REP(i,16) poss[i]=true;
		REP(k,2)
		{
			s(a);
			a--;
			REP(i,MN) REP(j,MN) s(grid[i][j]);
			REP(i,MN) REP(j,MN) poss[grid[i][j]-1]&=(i==a);
		}
		int c=0,stor;
		REP(i,16)
		{
			if(poss[i]) 
			{
				c++;
				stor=i+1;
			}
		}
		printf("Case #%d: ",cc+1);
		if(c==0) cout<<"Volunteer cheated!\n";
		else if(c>1) cout<<"Bad magician!\n";
		else cout<<stor<<endl;
	}
	return 0;
}
