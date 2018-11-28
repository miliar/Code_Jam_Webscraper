#include <stdio.h>
#include <string.h>
long long int T , r , t ,C = 1;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output","w",stdout);
	scanf("%I64d",&T);
	while ( T-- ){
		scanf("%I64d%I64d",&r,&t);
		long long front = (long long )(r+1)*(r+1) - r*r;
		
		long long left = 0 , right = 2147483647 , mid , ans = 0;
		while ( right >= left ){
			mid = (long long)( left + right ) >> 1;
			//printf("%I64d %I64d\n",mid,(front + (mid-1)*4 + front)*mid / 2);
			if ((long long) (front + (mid-1)*4 + front)*mid / 2 > t )
				right = mid-1;
			else
				ans = mid , left = mid + 1;
		}
		printf("Case #%I64d: %I64d\n",C++,ans);
	}
	
	
} 
