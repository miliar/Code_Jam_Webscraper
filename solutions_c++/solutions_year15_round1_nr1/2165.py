#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#define FOR(i,n) for(int i=0;i<n;++i)

using namespace std;


int max(int a,int b) { return a>b?a:b; }
int min(int a,int b) { return a<b?a:b; }

int main(void) {
	int t;
	int pole[20000];
	scanf("%d",&t);
	FOR(k,t) {
		int n;
		scanf("%d",&n);
		FOR(i,n) scanf("%d",&pole[i]);
		int ans1 = 0;
		for(int i=0;i<n-1;++i) {
			if(pole[i+1]<pole[i]) ans1+=pole[i]-pole[i+1];
		}
		int ans2=0;
		int m=0;
		for(int i=0;i<n-1;++i) {
			int q = pole[i]-pole[i+1];
			m = q>m?q:m;
		}
		int total = 0;
		for(int i=0;i<n-1;++i) {
			total=pole[i];
			int eat = min(m,total);
			ans2+= eat;
			total-=eat;
		}
		if(m>0 && total>pole[n-1]) ans2+=total-pole[n-1];
		printf("Case #%d: %d %d\n",k+1,ans1,ans2);
	}

}