#include<iostream>
#include<climits>
#define UINT long long
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	UINT testCases, caseCount, n,elemCount,sum,y,z,max,diff;

	cin>>testCases;
	for(caseCount =1; caseCount<=testCases; caseCount++)
	{
		cin>>n;
		UINT arr[n];
		y=z=0;
		max = 0;

		cin>>arr[0];
		for(elemCount =1 ;elemCount<n;elemCount++)
		{
			cin>>arr[elemCount];
			if(arr[elemCount-1]-arr[elemCount]>max)
			{
				max = arr[elemCount-1]-arr[elemCount];
			}
			
		}

		for(elemCount = 1; elemCount<n;elemCount++)
		{
			diff = arr[elemCount] - arr[elemCount-1];
			if(diff<0)
			{
				y+=-diff;
			}

			if(arr[elemCount-1]<max)
			{
				z+=arr[elemCount-1];
			}
			else
				z+=max;	
		}

		cout<<"Case #"<<caseCount<<": "<<y<<' '<<z<<endl;
	}

	return 0;
}




