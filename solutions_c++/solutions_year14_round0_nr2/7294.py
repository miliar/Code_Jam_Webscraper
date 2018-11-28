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
#define MN 100000

int main()
{	
	int T; s(T);
	REP(cc,T)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double mn=1e9;
		double add=2; double t=0,prev=-1;
		while(t<mn)
		{
			mn=min(mn,t+(X/add));
			prev=t;
			t+=(C/add);
			//cout<<C<<" "<<add<<" "<<t<<" "<<mn<<endl;
			add+=F;
		}
		printf("Case #%d: %.6lf\n",cc+1,mn);
	}
	return 0;
}
