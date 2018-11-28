#include <stdio.h>
#include <math.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		int D;
		scanf("%d",&D);
		char p[D];
		for(int j=0; j<D; j++){
			scanf("%d",p+j);
		}
		int max = 0;
		for(int j=0; j<D; j++){
			if(p[j] > max)
				max = p[j];
		}
		int ans = 9999999;
		for(int j=1; j<=max; j++){
			int tmp = j;
			for(int k=0; k<D; k++)
				tmp += ceil((p[k]-1)/j);
			if(tmp < ans){
				ans = tmp;
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
