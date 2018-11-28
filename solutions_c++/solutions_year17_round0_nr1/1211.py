#include<cstdio>
#include<cstring>

void solve(int case_num){
	char s[1001];
	int side[1000];
	int a[1000];
	int k;
	scanf("%s%d",s,&k);
	int n = strlen(s);
	for(int i=0;i<n;i++){
		if(s[i]=='+') side[i] = 0;
		else side[i] = 1;
	}
	int sum = 0;
	int ans = 0;
	for(int i=0;i+k<=n;i++){
		a[i] = (side[i] + sum) % 2;
		if((side[i]+sum)%2){
			sum++;
			ans++;
		}
		if(i-k+1>=0){
			sum -= a[i-k+1];
		}
	}
	bool flag = true;
	for(int i=n-k+1;i<n;i++){
		if((side[i]+sum)%2) flag = false;
		if(i-k+1>=0){
			sum -= a[i-k+1];
		}
	}
	printf("Case #%d: ",case_num);
	if(flag) printf("%d\n",ans);
	else printf("IMPOSSIBLE\n");
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) solve(i);
}
