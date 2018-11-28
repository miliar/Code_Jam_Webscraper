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
typedef pair<int,pii> piii;
#define MN 10000000
bool seen[10];
int main()
{	
	int T; s(T);
	REP(cc,T) {
		int n; s(n);	
		if(n==0) {
			printf("Case #%d: INSOMNIA\n",cc+1);
			continue;
		}
		REP(i,10) seen[i]=false;
		bool all=false;
		int i=1;
		while(!all) {
			int temp=n*(i++);
			while(temp!=0) {
				seen[temp%10]=true;
				temp/=10;
			}
			all=true;
			REP(i,10) all&=seen[i];
		}
		printf("Case #%d: %d\n",cc+1, n*(i-1));
	}
	return 0;
}