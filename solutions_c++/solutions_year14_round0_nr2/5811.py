#include <stdio.h>
#include <algorithm>

using namespace std;

double C,F,X;
double f(int n)
{
	double ret=0;
	for (int i=0; i<n; i++) {
		ret += C/(2+i*F);
	}
	return (X/(n*F+2)) + ret;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for (int z=1; z<=T; z++) {
		

		double min_v=2e9,v1,v2;
		scanf("%lf%lf%lf",&C,&F,&X);
		int l=0,h=100000,n;
		
		while (l<h)
		{
			n = (l+h)/2;
			v1 = f(n);
			v2 = f(n+1);
			if (v1<v2) {
				h=n-1;
				min_v = min(min_v, v1);
			}
			else if (v1>v2) {
				l=n+1;
				min_v = min(min_v, v2);
			}
			else {
				min_v = min(min_v, v2);
				break;
			}
		}

		printf("Case #%d: %.7f\n", z, min_v);

	}

	
}
