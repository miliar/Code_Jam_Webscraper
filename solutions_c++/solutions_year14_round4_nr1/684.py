#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
template<class T> T sqr(T x) {return x*x;}
#define pi acos(-1)
#define INF 100000000
#define debug(x) cerr<<#x"="<<(x)<<"\n";
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)

int a[11000];

int main() {
	int tt,te,n,m,i,j,ans;
	scanf("%d",&tt);
	for (te=1;te<=tt;te++) {
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++) scanf("%d",a+i);
		sort(a,a+n);
		reverse(a,a+n);
		ans=0;
		for (i=0,j=n-1;i<=j;i++) {
			ans++;
			if (i==j) break;
			if (a[i]+a[j]<=m) j--;
		}
		printf("Case #%d: %d\n",te,ans);
	}
}
