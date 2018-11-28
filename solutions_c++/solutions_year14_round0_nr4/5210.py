#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;
template<class T> T sqr(T x) {return x*x;}
#define pi acos(-1)
#define INF 100000000
#define debug(x) cerr<<#x"="<<x<<"\n";
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)

double a[2000],b[2000];
int v[2000];

int main() {
	int i,j,k,te,tt,n,a1,a2;
	scanf("%d",&tt);
	for (te=1;te<=tt;te++) {
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%lf",a+i);
		for (i=0;i<n;i++) scanf("%lf",b+i);
		sort(a,a+n);
		sort(b,b+n);
		a1=a2=0;
		memset(v,0,sizeof(v));
		for (i=0;i<n;i++) {
			k=-1;
			for (j=0;j<n;j++) if (!v[j])
				if (b[j]>a[i] && (k==-1 || b[j]<b[k])) k=j;
			if (k==-1) a2++;
			else v[k]=1;
		}
		memset(v,0,sizeof(v));
		for (i=0;i<n;i++) {
			k=-1;
			for (j=0;j<n;j++) if (!v[j])
				if (b[j]<a[i] && (k==-1 || b[j]<b[k])) k=j;
			if (k!=-1) {
				v[k]=1;
				a1++;
				continue;
			}
			k=-1;
			for (j=0;j<n;j++) if (!v[j])
				if (b[j]>a[i] && (k==-1 || b[j]>b[k])) k=j;
			if (k==-1) a1++;
			else v[k]=1;
		}
		printf("Case #%d: %d %d\n",te,a1,a2);
	}
}
