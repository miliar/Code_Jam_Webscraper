#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX 1010

FILE *input=freopen("input.txt","r",stdin);
FILE *output=freopen("output.txt","w",stdout);

double a[MAX];
double b[MAX];

int main()
{
	int n;
	int t;
	int tc=1;
	int i;
	int p,q;
	int ans1=0;
	int ans2=0;

	scanf("%d",&t);

	for(;t>0;t--)
	{
		ans1=0;
		ans2=0;

		scanf("%d",&n);

		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		
		p=n-1;
		q=n-1;

		sort(a,a+n);
		sort(b,b+n);

		while(1){
			if(p<0||q<0)
				break;
			if(a[p]>b[q])
			{
				p--;
				q--;
				ans1++;
			}
			else
				q--;
		}

		p=n-1;
		q=n-1;

		while(1){
			if(p<0||q<0)
				break;
			if(a[p]<b[q])
			{
				p--;
				q--;
				ans2++;
			}
			else
				p--;
		}

		printf("Case #%d: %d %d\n",tc++,ans1,n-ans2);
	}

	return 0;
}
