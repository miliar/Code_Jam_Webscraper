#include <cstdio>
#include <cstring>
int main()
{
	//freopen("PB.txt", "r", stdin);
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("PB.out", "w", stdout);
	int i, j, ans, cnt, ca=1;
	unsigned int A, B, K, TN;
	scanf("%d", &TN);
	while(TN--){
		scanf("%u%u%u", &A, &B, &K);
		ans=0;cnt=0;
		for(i=0;i<A;i++){
			for(j=0;j<B;j++){
				if((i&j)<K){
					//if(i==j)cnt++;
					ans++;
					//if(TN==4)
					//printf("%d %d = %d\n", i, j, ans);
				}
			}
		}
		
		printf("Case #%d: %d\n", ca++, ans-cnt);
	}
	return 0;
}