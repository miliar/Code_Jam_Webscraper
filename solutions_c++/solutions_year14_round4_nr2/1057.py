#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[1001];
int main()
{
	//freopen("PB.txt", "r", stdin);

	freopen("B-large.in", "r", stdin);
	freopen("PB-lar.out", "w", stdout);
	int TN, i, j, ca=1, N, n, ans, k;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d", &N);
		for(i=0;i<N;i++){
			scanf("%d", &a[i]);
			
		}
		int mnx;
		//if(ca>6)break;
		//for(k=0;k<N;k++)printf("%d ", a[k]);puts("");
		
		ans=0;n=N;
		for(i=0;i<n;){
		//	printf("a[%d] = %d\n", i, a[i]);
			mnx=i;
			for(j=i+1;j<n;j++){
				if(a[j]<a[mnx]){
					mnx=j;
					//printf("min a[%d] = %d\n", mnx, a[mnx]);

				}
			}
			//printf("i %d mnx %d\n", i, mnx);
			if(mnx-i==0){i++;continue;}
			if(mnx==n-1){n--;continue;}
			int tmp=a[mnx];
		
			if(mnx-i<=n-1-mnx){
				for(j=mnx;j>i;j--){
					a[j]=a[j-1];
				}
				a[i]=tmp;
				//printf("a %d\n", mnx-i);
			
				ans+=mnx-i;
				i++;
			}
			else{
				for(j=mnx;j<n-1;j++){
					a[j]=a[j+1];
				}
				a[n-1]=tmp;
				ans+=n-1-mnx;

				//printf("b %d\n", n-1-mnx);
				n--;
			}
			//printf("n: %d\n", n);
			//for(k=0;k<N;k++)printf("%d ", a[k]);puts("");
		
			
		}
		printf("Case #%d: %d\n", ca++, ans);

	}
	return 0;
}