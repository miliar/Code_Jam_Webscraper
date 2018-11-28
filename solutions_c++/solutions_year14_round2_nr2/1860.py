#include<cstdio>
int tmp[1001]={0};
void solve(int C) {
	int a,b,c;
	printf("Case #%d: ",C);
	scanf("%d%d%d",&a,&b,&c);
	for(int i=0;i<a;i++) {
		for(int j=0;j<b;j++) {
			int x=i&j;
			if(x<c) tmp[x]++;
		}
	}
	int ans=0;
	for(int i=0;i<c;i++) {
		ans+=tmp[i];
		tmp[i]=0;
	}
	printf("%d\n",ans);
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		solve(t+1);
	}
	return 0;
}