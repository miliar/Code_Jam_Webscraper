#include<cstdio>
int n,ans,T;
char ch[1010];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;++test){
		ans=0;
		int k=0;
		scanf("%d%s",&n,ch);
		for(int i=0;i<=n;++i){
			if(k<i){
				ans+=i-k;
				k=i;
			}
			k+=ch[i]-'0';
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
} 
