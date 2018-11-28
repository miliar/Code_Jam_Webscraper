#include <cstdio>
char str[2001];
int main(){
 	int T,ans,cnt;
 	int s;
	scanf("%d",&T);
	for(int j=1;j<=T;j++){
		ans=cnt=0;
		scanf("%d %s",&s,str);
		for(int i=0;i<=s;i++){
			if(cnt < i&&str[i]!='0'){
				ans+=i-cnt;
				cnt+=ans;
			}
			cnt+=str[i]-'0';
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}
