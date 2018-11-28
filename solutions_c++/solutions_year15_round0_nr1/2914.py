#include <stdio.h>
#include <iostream>
#include <cstdlib>
int ans[100005];
char q[100005];

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int n,m,T=1;
	scanf("%d",&n);
	while(n--){
		scanf("%d",&m);
		scanf(" %s",q);
		for(int i=0;i<m+1;i++){
			ans[i]=q[i]-'0';
		}
		int aa=0,sum=0;
		for(int t=0;t<m+1;t++){
		    if(ans[t]==0)continue;

			if(sum<t){
				aa+=(t-sum);
				sum= t;
				sum+=ans[t];
			}
			else{
				sum+=ans[t];
			}

		}
		printf("Case #%d: %d\n",T++,aa);
	}

	return 0;
}
