#include <iostream>
#include <algorithm>
using namespace std;
double  a[1001],b[1001];
// strategy of b, min bi>a or min bi if not exists
// if maxiam b > maxima a,  use minimal a to remove maxima a
// if maxiam b < maxima a,  a win for sure, remove minimal b
int main()
{
	int  Cases;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&Cases);
	for (int i = 1; i<= Cases; ++i)
	{
		printf("Case #%d: ", i);
	    int n;
		scanf("%d",&n);
		for(int j=0;j<n;++j) scanf("%lf",&a[j]);
		sort(a,a+n);
		//for(int j=0;j<n;++j) printf("%lf ",a[j]);
		for(int k=0;k<n;++k) scanf("%lf",&b[k]);
		sort(b,b+n);
		//printf("\n");
		//for(int j=0;j<n;++j) printf("%lf ",b[j]);
		//printf("\n");
		int min_a = 0, min_b = 0, point=0;
		for(int j=0;j<n;++j)
		{
			if(b[min_b]> a[min_a])++min_a;
			else 
			{
				++point;
				++min_a;
				++min_b;
			}
		}
		min_a = 0, min_b = 0;
		int point2=0;
		for(int j=0;j<n;++j)
		{
			if(b[min_b]> a[min_a])
			{
				++min_a;
				++min_b;
			}
			else 
			{
				++point2;
				++min_b;
			}
		}
		printf("%d %d\n",point,point2);

	}
	return 0;
}