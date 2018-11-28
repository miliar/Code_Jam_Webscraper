#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main ()
{
	ofstream output;
	output.open ("output.txt");

	int i=0, j=0, k=0;
	int t=0, n=0, sum1=0, sum2=0;

	scanf ("%d", &t);

	for (i=0; i<t; i++)
	{
		scanf("%d", &n); 
		double a[n];
		double b[n]; 

		for (j=0; j<n; j++)
		{
			scanf("%lf", &a[j]);
		}
		for (j=0; j<n; j++)
		{
			scanf("%lf", &b[j]);
		}

		sort (a, a+n);
		sort (b, b+n);

		//j=n-1;
		//k=n-1;
		j=0; k=0;
		while (j<n)
		{
			if (a[j]>b[k])
			{
				sum1=sum1+1;
				j=j+1;
				k=k+1;
			}
			else
			{
				j=j+1;
			}
		}

		j=n-1;
		k=n-1;
		while (j>=0)
		{
			if (a[j] > b[k])
			{
				sum2=sum2+1;
				j=j-1; 
			}
			else
			{
				j=j-1;
				k=k-1;
			}
		}

		//printf("Case #%d: %d %d\n", (i+1), sum1, sum2);
		output<<"Case #"<<(i+1)<<": "<<sum1<<" "<<sum2<<"\n";
		sum2=0;
		sum1=0;


	}


	output.close();
	return 0;
}