#include <cstdio>
#include <algorithm>

using namespace std;
int main()
{
	int t,n,i,j,c,d,x=1;
	scanf("%d",&t);
	while(t--) {
		c = 0;
		d = 0;
		scanf("%d",&n);
		long double a[n],b[n];
		for(i = 0; i < n; i++)
			scanf("%Lf",&a[i]);
		for(i = 0; i < n; i++)
			scanf("%Lf",&b[i]);
		
		sort(a,a+n);
		sort(b,b+n);
		i = j = 0;
		while(j < n) {
			if(b[j] > a[i]) {
				c++;
				i++;
				j++;
			}
			else {
				j++;
			}
		}
		i = j = 0;
		while(j < n) {
			if(a[j] > b[i]) {
				d++;
				i++;
				j++;
			}
			else {
				j++;
			}
		}
		printf("Case #%d: %d %d\n",x,d,n-c);
		x++;
	}	
	return 0;
}
