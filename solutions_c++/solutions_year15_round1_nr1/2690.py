#include <iostream>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++)
	{
		cout<<"Case #"<<tc<<": ";
		long long int sum1=0,sum2=0;
		int n,max1=0;
		scanf("%d",&n);
		int a[n];

		for(int i=0; i<n; i++)
			scanf("%d",&a[i]);

		for(int i=1; i<n; i++)
		{
			if(a[i-1]>a[i])
			{
				sum1+= a[i-1]-a[i];
				if((a[i-1]- a[i])>max1 ) max1= a[i-1]-a[i];
			}
		}

		for( int i=0; i<n-1; i++)
		{

			if( a[i]<max1 ) sum2+=a[i];
			else sum2+=max1;
		}

		printf("%lld %lld\n",sum1,sum2);

	}
}