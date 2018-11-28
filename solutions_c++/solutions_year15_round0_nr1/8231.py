#include <cstdio>
#include <cstring>
const int MAXN = 1005;
int t,ca;
char input[MAXN];
int cnt[MAXN],n;

int solve(){
	int sum=0,ans=0;
	for(int i=0;i<=n;i++){
		if(sum<i){
			ans += (i-sum);
			sum = i;
		}
		sum += cnt[i];
	}
	return ans;
}

int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d %s",&n,input);
		for(int i=0;i<=n;i++) cnt[i]=input[i]-48;
		printf("Case #%d: %d\n",++ca,solve());
		
	}
	return 0;
}
