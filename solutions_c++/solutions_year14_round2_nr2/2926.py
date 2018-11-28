#include <cstdio>
#include <cstdlib>

int main(){
	int tt, c=1;
	int a,b,k;
	int i,j;
	int ans;
	int x;
	scanf("%d",&tt);
	while(tt>0){
		ans = 0;
		scanf("%d %d %d",&a, &b, &k);
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				if ((i&j) < k){
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",c,ans);
		c++;tt--;
	}
	return 0;
}
