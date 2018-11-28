#include <stdio.h>
long long int f(long long int a[], int size){
	long long int maxdiff=0;
	for (int i = 0; i < size-1; ++i)
		if ((a[i]-a[i+1])>maxdiff)
			maxdiff = (a[i]-a[i+1]);
	return maxdiff;
}
int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int totalCases;	scanf("%d", &totalCases);
	for (int caseNo = 1; caseNo <= totalCases; ++caseNo)
	{
		int n;	long long int sum=0, sum2=0, maxdiff;	scanf("%d", &n);
		long long int *m = new long long int[n];
		for (int i = 0; i < n; ++i)
			scanf("%lld", &m[i]);
		maxdiff = f(m, n);
		for (int i = 0; i < n-1; ++i)
			if (m[i]-m[i+1]>0)
				sum += (m[i]-m[i+1]);
		for (int i = 0; i < n-1; ++i) {
			if (m[i]<maxdiff)
				sum2 += m[i];
			else
				sum2 += maxdiff;
		}
		printf("Case #%d: %lld %lld\n", caseNo, sum, sum2);		
	}
	return 0;
}