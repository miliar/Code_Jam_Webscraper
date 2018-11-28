#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

const int maxn=1005;

int main() {
	int T,n,ans1,ans2;
	double a[maxn],b[maxn];
	freopen("ddfdafda.txt","w",stdout);
	freopen("D-large.in","r",stdin);
	scanf("%d",&T);
	for(int TT=1; TT<=T; TT++) {
		scanf("%d",&n);
		for(int i=0; i<n; i++) {
			scanf("%lf",&a[i]);
		}
		for(int i=0; i<n; i++) {
			scanf("%lf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		ans2=0;
		for(int i=0,j=0; j<n;) {
			while(j<n && b[j]<a[i]) j++;
			if(j < n) {
				ans2++;
				i++;
				j++;
			}
		}
		ans2=n-ans2;
		ans1=0;
		for(int i=0,j=0; i<n;) {
			while(i<n && a[i]<b[j]) i++;
			if(i < n) {
				ans1++;
				i++;j++;
			}
		}
		printf("Case #%d: %d %d\n",TT,ans1,ans2);
	}
	return 0;
}