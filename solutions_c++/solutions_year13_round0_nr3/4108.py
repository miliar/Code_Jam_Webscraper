#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
int g[110][110];
int dp[10001000];
typedef long long LL;
bool check(LL x){
	int  str[20];
	int p=0;
	while(x){
		str[p++]=x%10;
		x/=10;
	}
	for(int i=0,j=p-1;i<j;i++,j--){
		if(str[i]!=str[j])
			return false;
	}
	return true;
}
void prework(){
	dp[1]=1;
	for(int i=2;i<10001000;i++){
		LL x=i*1ll*i;
		if(check(x)&&check(i)){
			dp[i]=dp[i-1]+1;
		}else{
			dp[i]=dp[i-1];
		}
		//if(x>=100&&x<=1000)printf("%I64d\n",x);
	}
}
int main(){
	freopen("C-large-1.in","r",stdin);
	freopen("o.out","w",stdout);
	int T,cas=1;
	scanf(" %d",&T);
	prework();
	while(T--){
		LL a,b;
		scanf(" %I64d %I64d",&a,&b);
		int a1=sqrt(a+0.),a2=sqrt(b+0.);
		if(a1*1ll*a1==a){
			a1--;
		}
		printf("Case #%d: %d\n",cas++,dp[a2]-dp[a1]);
	}
	return 0;
}
