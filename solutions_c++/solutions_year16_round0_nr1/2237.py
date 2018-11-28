#include <stdio.h>
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	int a;
	int ans;
	bool over;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d",&a);
		if(a==0){
				ans =-1;
		}
		else {
			int h[10];
			for(int t=0;t<10;t++){
				h[t] = 0;
			}
			over =true;
			ans= 0;
			while(over){
				ans++;
				int na = a*ans;
				while(na!=0){
					int yu  = na%10;
					na= na/10;
					if(h[yu]==0){
						h[yu]=1;
						for(int j=0;j<10;j++){
							if(h[j]!=1)break;
							if(j==9)over =false;
						}
					}
				}
			}

		}
		if(ans == -1){
			printf("Case #%d: INSOMNIA\n",cs);
		}
		else{
			printf("Case #%d: %d\n",cs,ans*a);
		}

	}
	return 0;
}
