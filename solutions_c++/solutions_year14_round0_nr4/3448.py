#include<bits/stdc++.h>

using namespace std;

bool comparator(double x, double y)
{
	return x>y;
}

int main(void)
{
	int t;
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		int n;
		cin >> n;
		double arr[n];
		double brr[n];
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&arr[i]);
		}
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&brr[i]);
		}
		sort(arr, arr+n);
		sort(brr, brr+n, comparator);
		
		int dcount = 0;
		int sp = 0,ep = n-1;
		int ii = 0;
		while(ii<n)
		{
			if(arr[ii] <= brr[ep])
			{
				sp+=1;
				ii++;
			}
			else
			{
				ep-=1;
				ii++;
				dcount++;
			}
		}
		
		int wcount = 0;
		sp = 0, ep = n-1;
		ii = n-1;
		while(ii>=0)
		{
			if(arr[ii] >= brr[sp])
			{
				ep-=1;
				ii--;
				wcount++;
			}
			else
			{
				sp+=1;
				ii--;
			}
		}
		
		cout << "Case #" << T << ": ";
		printf("%d %d\n",dcount,wcount);		
	}
}
