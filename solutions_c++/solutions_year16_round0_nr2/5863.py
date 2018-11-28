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
int main()
{	
	int T; s(T);
	REP(cc,T) {
		string in; cin>>in;
		in+="+";
		int c=0;
		for(int i=1;i<in.length();i++) {
			if(in[i-1]!=in[i]) c++;
		}
		printf("Case #%d: %d\n",cc+1,c);
	}
	return 0;
}