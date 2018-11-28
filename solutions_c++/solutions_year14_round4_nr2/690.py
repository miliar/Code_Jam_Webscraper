#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
template<class T> T sqr(T x) {return x*x;}
#define pi acos(-1)
#define INF 100000000
#define debug(x) cerr<<#x"="<<(x)<<"\n";
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)

int a[1100];

int main() {
	int te,tt,l,r,i,j,k,n,ans;
	scanf("%d",&tt);
	for (te=1;te<=tt;te++) {
		scanf("%d",&n);
		for (i=1;i<=n;i++) scanf("%d",a+i);
		l=0;r=n+1;
		ans=0;
		for (i=1;i<=n;i++) {
			k=l+1;
			for (j=l+1;j<=r-1;j++) if (a[j]<a[k]) k=j;
			if (k-l<r-k) {
				l++;
				for (j=k;j>l;j--) swap(a[j],a[j-1]),ans++;
			}
			else {
				r--;
				for (j=k;j<r;j++) swap(a[j],a[j+1]),ans++;
			}
		}
		printf("Case #%d: %d\n",te,ans);
	}
}
