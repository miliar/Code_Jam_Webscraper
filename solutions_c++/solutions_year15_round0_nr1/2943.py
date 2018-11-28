#include <cstdio>
int abc;
int rnd=1;
char cmd;
int a[2000];
int now;
int n;
int ans;
void solve(){
	scanf("%d",&n);
	for(int i=0;i<=n;i++){
		scanf(" %c",&cmd);
		a[i]=cmd-'0';
	}
	ans=0;
	now=0;
	for(int i=0;i<=n;i++){
		if(now<i){
			ans+=i-now;
			now=i;
		}
		now+=a[i];
	}
	printf("CASE #%d: %d\n",rnd++,ans);
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&abc);
	while(abc--) solve();
	return 0;
}