#include <stdio.h>
#include <cstring>
int n;
char s[1005];
int f(){
	int i,x;
	int cnt = 0;
	int res = 0;
	for(i=0;i<=n;i++){
		x = s[i] - '0';
		if(cnt < i && x > 0){
			res += (i-cnt);
			cnt += (i-cnt);
		}
		cnt += x;
	}
	return res;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,C;
	scanf("%d",&T);
	for(C=1;C<=T;C++){
		printf("Case #%d: ",C);
		scanf("%d %s",&n,s);
		printf("%d\n",f());
	}
}