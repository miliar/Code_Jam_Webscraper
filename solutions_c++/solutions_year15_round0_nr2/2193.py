#include<cstdio>

using namespace std;

#define MAX_PAN 1010
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

int main(void)
{
	int cases;
	int cas;
	scanf("%d",&cases);
	int D;
	int pan[MAX_PAN];
	int i,j;
	int ans;
	int p_max;

	for(cas=1;cas<=cases;cas++){
		ans=0;
		p_max=0;
		scanf("%d",&D);
		
		for(i=0;i<D;i++){
			scanf("%d",&pan[i]);
			p_max=max(pan[i],p_max);
		}
		
		
		ans=p_max;
		for(i=1;i<=p_max;i++){
			int tmp=0;
			for(j=0;j<D;j++){
				tmp+=pan[j]/i;
				if(pan[j]%i==0)
					tmp--;
			}
			tmp+=i;
			ans=min(ans,tmp);
			
		}

		
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}
