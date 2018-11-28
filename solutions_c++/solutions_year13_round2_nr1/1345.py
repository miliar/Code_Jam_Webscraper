#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

long long nA;

int calc (long long  A,long long X)
{
	long long cur;
	int k = 0;
	while (A<=X)
	{
		cur = A-1;
		A+=cur;
		k++;
	}
	nA = A;
	return k;
}

int main ()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int t,c=1;
	scanf ("%d",&t);
	while (t--)
	{
		long long A,arr[110];
		int n,i,j;
		long long k;
		int op = 0,lop;
		
		scanf ("%lld %d",&A,&n);
		for (i=0;i<n;i++)
			scanf ("%lld",&arr[i]);
		sort (arr,arr+n);

		int ret = n;

		for (i=0;i<n;i++)
		{
			if (arr[i]<A)
			{
				A += arr[i];
				continue;
			}
			long long TBD = A - 1LL;
			if (!TBD)
			{
				lop--;
				op++;
				continue;
			}
			ret = min (ret,op+n-i);
			k = calc(A,arr[i]);
			A = nA;
			A +=arr[i];
			lop -= k;
			op += k;
		}
		ret = min (ret,op+n-i);
		printf ("Case #%d: ",c++);
		cout << ret << endl;
	}

	return 0;
}
