#include<stdio.h>
#include<math.h>
#include<string.h>

int main(void){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);    

	int T, cnt=1;
	bool flag = true;
	long long r, t,k = 1,ans = 0 ;

	scanf("%d",&T);

	while(T-->0){
		scanf("%lld %lld",&r,&t);

		while(flag){
			if(t >= (2*k*(k+1)+k*(2*r-3))){
				ans++; k++;
				continue;
			}
			break;
		}
		printf("Case #%d: %lld\n", cnt++,ans);
		ans = 0; k = 1;
	}
}