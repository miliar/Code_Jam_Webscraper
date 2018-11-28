#include <stdio.h>
#include <iostream>
#include <cstdlib>
using namespace std;
int eat[1005];
int maxt;
int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int n,m,T=1;
	int ans;
	scanf("%d",&n);
	while(n--){
			maxt=0;
		scanf("%d",&m);
		for(int i=0;i<m;i++){
			scanf("%d",&eat[i]);
			maxt = max(eat[i],maxt);
		}
		ans =99999;
		int st;
		for(int t=1;t<=maxt;t++){
			st=0;
			for(int i=0;i<m;i++){
				st+=(eat[i]/t-1);
				if(eat[i]%t!=0){
					st++;
				}
			}
			ans =min(ans,t+st);
		}
		printf("Case #%d: %d\n",T++,ans);
	}

	return 0;
}
