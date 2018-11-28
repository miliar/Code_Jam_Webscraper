#include <stdio.h>
#include <algorithm>
#define MAX 1001

int main(){
	int t,i,j,k,n,dw,w;

	double a[MAX],b[MAX];

	scanf("%d",&t);

	for(i = 1;i<=t;i++){
		scanf("%d",&n);

		for(j = 0;j<n;j++)
			scanf("%lf",&a[j]);

		for(j = 0;j<n;j++)
			scanf("%lf",&b[j]);

		sort(a,a+n);
		sort(b,b+n);

		dw = w = 0;

		for(j = 0,k=0;j<n;j++)
			if(a[j] > b[k]){
				k++;
				dw++;
			}

		for(j = n-1,k=n-1;j>=0;j--){
			if(a[j] < b[k])
				k--;
			else
				w++;
		}

		printf("Case #%d: %d %d\n",i,dw,w);
	}

	return 0;
}