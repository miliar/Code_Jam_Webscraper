#include<cstdio>
#include<iostream>
using namespace std;

int main()
{	int t;
	cin>>t;
	for ( int l=1; l<=t; l++ )
	{	long double c,f,x;
		cin>>c>>f>>x;
		long double sum=0, sf=2, sum1, sum2;
		if ( x <= c )
		{	sum= x/sf;
			printf("Case #%d: %0.7Lf\n", l, sum);
			continue;
		}
		do
		{	sum += (long double) c/sf;
			sum1= (x-c)/sf;
			sum2=  x/(sf+f);
			//cout<<sf<<" "<<c/sf<<" "<<sum1<<endl;
			if ( sum1 >= sum2 )
				sf += f;
		} while ( sum1 >= sum2 );
		sum += sum1;
		printf("Case #%d: %0.7Lf\n", l, sum);
	}
	return 0;
}
