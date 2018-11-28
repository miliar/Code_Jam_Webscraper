#include <iostream>
#include <cstdio>
#include <algorithm>
#define lli long long int
using namespace std;

int compare_function(const void *a,const void *b) {
double *x = (double *) a;
double *y = (double *) b;

if (*x < *y) return -1;
else if (*x > *y) return 1;
return 0;
}

int main() {
	// your code goes here
	lli tcase,li,n,i,j,k,count1,count2,strt1n,strt2n,strt1k,strt2k,end1k,end2k,end1n,end2n;
	
	scanf("%lld", &tcase);
	
	for (li = 1; li <= tcase; ++li) {
		scanf("%lld", &n);
		
		double a[n],b[n];
		
		for (i = 0; i < n; ++i)
			scanf("%lf", &a[i]);
		
		for (i = 0; i < n; ++i)
			scanf("%lf", &b[i]);
			
		qsort(a,n,sizeof(double),compare_function);
		qsort(b,n,sizeof(double),compare_function);
	/*	
		for (i = 0; i < n; ++i) {
			printf("%lf ", a[i]);
		}
		printf("\n");
		
		for (i = 0; i < n; ++i) {
			printf("%lf ", b[i]);
		}
		printf("\n");
	*/
		strt1n = 0;
		strt2n = 0;
		strt1k = 0;
		strt2k = 0;
		count1 = 0;
		count2 = 0;
		end1n = n-1;
		end2n = n-1;
		end1k = n-1;
		end2k = n-1;
		
		for (i = 0; i < n; ++i) {
	//		cout << a[end1n] << " " << b[end2n] << endl;
			if (a[end1n] > b[end2n]) {
				++count1;
				--end1n;
				--end2n;
	//			cout << "hi "  << endl;
			} else {
				++strt1n;
				--end2n;
			}
			
			if (b[end2k] > a[end1k]) {
				++count2;
				--end2k;
				--end1k;
			} else {
				++strt2k;
				--end1k;
			}
		}
		
		printf("Case #%lld: %lld %lld\n", li, count1, n - count2);
	}
	return 0;
}
