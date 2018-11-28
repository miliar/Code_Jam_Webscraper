#include <cstdio>
#include <cstring>
const int N = 1010;
char buf[N];
int main(){
	int T;
	scanf("%d",&T);
	int count = 0;
	while(count++ < T){
		int S;
		scanf("%d",&S);
		scanf("%s",buf);
		int now = 0;
		int ans = 0;
		int len = strlen(buf);
		for(int i = 0; i <= S; i++){
			int oao = buf[i] -'0';
			if(oao != 0 && i > now){
				ans += (i-now);
				now = i+oao;
			}
			else now += oao;
		}
		printf("Case #%d: %d\n",count,ans);
	}

}
