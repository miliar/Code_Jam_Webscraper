#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
int abc;
int rnd=1;
char cmd;
int a[2000];
int now;
int n,x,f,s,t2,t1,tmp;
int ans,mini,mx;
priority_queue<int> h;
void solve(){
	scanf("%d",&n);
	while(!h.empty()) h.pop();
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	mini=0;
	ans=999999999;
	for(int i=1;i<=1000;i++){
		mini=0;
		mx=0;
		for(int j=1;j<=n;j++){
			if(a[j]<=i){if(a[j]<mx)mx=j;continue;}
			else{
				mini+=(a[j])/i;
				if(a[j]%i==0) mini--;
			}
		}
		//printf("%d %d\n",i,mini);
		if(max(mx,i)+mini<ans) ans=mini+max(mx,i);
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