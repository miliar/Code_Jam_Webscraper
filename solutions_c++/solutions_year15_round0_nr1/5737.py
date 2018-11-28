#include<cstdio>
#include<cstring>
int T,n;
char a[1111];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		memset(a,0,sizeof(a));
		scanf("%d ",&n);
		scanf("%s",a);
		int cnt=a[0]-'0',ans=0;
		for(int i=1;i<=n;i++){
			if(i>cnt&&a[i]-'0'>0)ans+=i-cnt,cnt+=i-cnt;
			cnt+=a[i]-'0';
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
