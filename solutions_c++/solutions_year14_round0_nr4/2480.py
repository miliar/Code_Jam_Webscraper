#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int t,i,n,j,k;
	int x,z;
	double arr[1002],brr[1002],a[1002],b[1002];
	scanf("%d", &t);
	for(i=0;i<t;i++) {
		x = 0;
		z = 0;
		scanf("%d", &n);
		for(j=0;j<n;j++) {
			scanf("%lf", &arr[j]);
			a[j] = arr[j];
		}
		for(j=0;j<n;j++) {
			scanf("%lf", &brr[j]);
			b[j] = brr[j];
		}
		sort(arr,arr+n);
		sort(brr,brr+n);
		sort(a,a+n);
		sort(b,b+n);
		
		for(j=0;j<n;j++) {
						
			for(k=0;k<n;k++) {
				if(arr[k] > brr[j]) {
					arr[k] = 0;
					brr[j] = 0;
					x++;
					break;
				}
			}
		}
		for(j=0;j<n;j++) {
			
			for(k=0;k<n;k++) {
				if(b[k] > a[j]) {
					z++;
					b[k] = 0;
					a[j] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i+1,x,n-z);
	}
	return 0;
}
