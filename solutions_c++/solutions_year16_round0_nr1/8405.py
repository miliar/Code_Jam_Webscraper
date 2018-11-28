#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,x;
	bool vis[10];
	int visited;
	long long ans;
	scanf("%d",&T);
	for(int i = 1; i <= T; i++){
		scanf("%d",&x);
		memset(vis,0,sizeof(vis));
		visited = 0;
		printf("Case #%d: ",i);
		if(x == 0){
			puts("INSOMNIA");
		}
		else{
			for(int j = 1; visited < 10; j++){
				long long tmp = j*(long long)(x);
				ans = tmp;
				while(tmp){
					if(!vis[tmp%10]){
						visited++;
					} 
					vis[tmp%10]=true;
					tmp/=10;
				}
			}
			printf("%lld\n",ans);
		}
	} 
	return 0;
} 
