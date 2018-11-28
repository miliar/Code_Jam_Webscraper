#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef long long ll;
int sum[1111];
char s[1111];
int main(){
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	int t,n;
	scanf("%d",&t);
	while(t--){
		static int cas=1;
		printf("Case #%d: ",cas++);
		scanf("%d%s",&n,s);
		sum[0]=s[0]-'0';
		for(int i=1;s[i];++i) sum[i]=sum[i-1]+s[i]-1;
		int ans=0,m=0;
		for(int i=0;i<=n;++i){
			if(s[i]=='0') continue;
			if(m>=i) m+=s[i]-'0';
			else ans+=i-m,m=i+s[i]-'0';
		}
		printf("%d\n",ans);
	}
	return 0;
}
