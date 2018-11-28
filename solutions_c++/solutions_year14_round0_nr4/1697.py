#include <stdio.h>
#include <algorithm>
using namespace std;

const int mx = 1010;

int n;
double a[mx],b[mx];

int cal(double p[],double q[])
{
	int cnt = 0;
	int i,j = 0;
	for(i=0;i<n&&j<n;i++)
	{
		while( j<n && p[i] > q[j] ) 
		{
			j++;
			cnt++;
		}
		j++;
	}
	return cnt;
}

int main()
{
	int T;
	int ca = 1;
	int i,j;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf",&a[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%lf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: %d %d\n",ca++,n-cal(b,a),cal(a,b));
	}
	return 0;
}

