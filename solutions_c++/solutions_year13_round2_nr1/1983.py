#include <stdio.h>
#include <algorithm>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,k=0;
	scanf("%d",&T);

	while (++k<=T)
	{
		int a,n,i,ret=0;
		int *M = new int[1000010];
		scanf("%d%d",&a,&n);	
		for (i=1; i<=n; i++) 
			scanf("%d",M+i);
		std::sort(M+1,M+1+n);

		for (i=1; i<=n; i++) {
			if (M[i] < a) a+=M[i];

			else {
				int cnt=0;
				while (M[i] >= a && cnt<=n) a+=a-1,cnt++;
				a+=M[i];
				if (cnt < n-i+1) ret+=cnt;
				else {ret+=n-i+1;break;}
			}
		}

		printf("Case #%d: %d\n",k,std::min(ret,n));
		delete M;
	}
}
/*



*/
