#include <cstdio>

int a[1010];
int n;

int main(){
	int nt=0;
	scanf("%d", &nt);
	for (int T=1; T<=nt; ++T){
		scanf("%d", &n);
		int ans=-1;
		for (int i=0; i<n; ++i)
			scanf("%d", a+i);
		for (int i=1; i<=1000; ++i){
			int t=i;
			for (int j=0; j<n; ++j)
				t+=(a[j]-1)/i;
			if (t<ans || ans==-1) ans=t;
		}
		printf("Case #%d: %d\n", T, ans);
	}
}
