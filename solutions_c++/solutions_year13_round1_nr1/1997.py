#include<stdio.h>
#include<math.h>

int main()
{
	long long int t,no;
	scanf("%lld", &t);
	long long int k;
	for(k = 0;k < t;k++) {
		double r,y;
		scanf("%lf%lf", &r, &y);
		double i;
		double to;
		to = (r+1)*(r+1) - r*r;
	//	 printf("%lf\t", to);
		no = 1;
		for(i = r+3;to <= y;i +=2 ) {
			to += (i*i) - (i-1)*(i-1);
	//		printf("%lf\t", to);
		       	if(to <= y)
				no++;
		}
	printf("Case #%lld: %lld\n",k+1, no);
	}
	return 0;
}	
