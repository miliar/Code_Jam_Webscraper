#include <cstdio>
#include <algorithm>
const int MAXN=1005;
int main(){
	int T;
	float a[MAXN],b[MAXN];
	scanf("%d",&T);
	for(int caseNumber=1;caseNumber<=T;++caseNumber){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i) scanf("%f",a+i);
		for(int i=0;i<n;++i) scanf("%f",b+i);
		std::sort(a,a+n);
		std::sort(b,b+n);
		int cnt1=0;
		int p=0,q=n-1;
		for(int i=0;i<n;++i){
			if(a[i]<b[p]) --q;
			else{
				++cnt1;
				++p;
			}
		}
		int cnt2=0;
		p=0;
		for(int i=0;i<n;++i){
			for(;(b[p]<a[i])&&(p<n);++p);
			if(p>=n) break;
			++cnt2;
			++p;
		}
		cnt2=n-cnt2;
		printf("Case #%d: %d %d\n",caseNumber,cnt1,cnt2);
	}
}
