#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef pair<int,int> PII;
const double eps = 1e-7;
const double PI = acos(-1.0);
const int oo = 1<<29;

const int N = 110;
const int P = 1000002013;

int calc(int n,int len) {
	int ret=0;
	int now=n;
	for(int i=0;i<len;i++) {
		ret+=now;
		now--;
	}
	return ret;
}

int main()
{
	int T; scanf("%d",&T);
	int n,m;
	for(int ka=1;ka<=T;ka++) {
		scanf("%d%d",&n,&m);
		int a[N];
		mem(a,0);
		int all=0;
		for(int i=0;i<m;i++) {
			int s,t; scanf("%d%d",&s,&t);
			int p; scanf("%d",&p);
			all+=calc(n,t-s)*p;
			if(s==t) continue;
			for(int j=s;j<t;j++) a[j]+=p;
		}

		int ans=0;
		while(1) {
			int i;
			for(i=1;i<=n;i++) if(a[i]) break;
			if(i>n) break;
			int mn=a[i];
			int st=i;
			for(;; i++) {
				mn=min(mn,a[i]);
				if(a[i+1]==0) break;
				if(i==n) break;
			}
			ans+=calc(n,i+1-st)*mn;
			for(int j=st;j<=i;j++) a[j]-=mn;
		}

		ans=all-ans;
		ans%=P;
		printf("Case #%d: %d\n",ka,ans);
	}

	return 0;
}
