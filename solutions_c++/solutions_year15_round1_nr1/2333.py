#include<iostream>
#include<cstdio>
using namespace std;
int n, a[10001];

void solve(){
	scanf("%d", &n);
	for(int i = 1; i<=n;i++)
		scanf("%d",&a[i]);
	int ans1= 0, diff= 0;
	for(int i = 2; i<=n;i++)
		if(a[i]<a[i-1]){
			ans1+=a[i-1]-a[i];
			diff = max(diff, a[i-1]-a[i]);
		}
	printf("%d ", ans1);

	int s = a[1], ans2=0;
	for(int i = 1; i < n; i++){
		ans2+=min(s, diff);
		s-=min(s,diff);
		s=a[i+1];
	}
	printf("%d\n", ans2);
}


int main(){
	freopen("t1.in", "r", stdin);
	freopen("t1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i<=t;i++){
		printf("Case #%d: ", i);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
