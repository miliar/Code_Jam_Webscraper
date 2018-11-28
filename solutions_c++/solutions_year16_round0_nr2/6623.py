#include <cstdio>
#include <cstring>
int main(){
	freopen("/Users/shintaku/Desktop/B-large.in","r",stdin);
    freopen("/Users/shintaku/Desktop/B-large.out","w",stdout);
	int t,cas=0;
	char str[101];
	scanf("%d",&t);
	while(t--){
		scanf("%s",str);
		int i,ans=0;
		for(i=0;i<strlen(str)-1;i++){
			if(str[i]!=str[i+1]) ans++;
		}
		if(str[i]=='-') ans++;
		printf("Case #%d: %d\n",++cas,ans);
	}
}