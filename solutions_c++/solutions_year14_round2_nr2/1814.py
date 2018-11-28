#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int t,a,b,n,ans;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for ( int i = 1; i <= t; ++ i){
		printf("Case #%d: ",i);
		scanf("%d%d%d",&a,&b,&n);
		ans = 0;
		for ( int j = 0; j < a; ++ j)
			for ( int k = 0; k < b; ++ k)
				if ((j & k) < n) ++ ans;
		printf("%d",ans);
		printf("\n");
	}

	return 0;
}
