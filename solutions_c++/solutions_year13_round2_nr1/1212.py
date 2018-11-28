#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
int main()
{
	freopen ("output.txt","w",stdout);
	freopen ("input.txt","r",stdin);
	long long T,n,s,arr[103],arr2[103]={0};
	cin>>T;
	for(int F=1;F<=T;F++)
	{
		cin>>s>>n;
		for(int f=0;f<n;f++)
			cin>>arr[f];
		sort(arr,arr+n);
		int to=0,o=0;
		if(s==1)
			to=n;
		else
		{
			for(int f=0;f<n;f++)
			{
				if(s>arr[f])
				{	
					arr2[f+1]=o+arr2[f];
					s+=arr[f];
					o=0;
				}
				else
				{
					o++;
					s+=(s-1);
					f--;
				}
			}
			to=n;
			for(int f=1;f<=n;f++)
			{
				if(to>n-f+arr2[f])
				{
					to=n-f+arr2[f];
					//break;
				}
			}
		}
		cout<<"Case #"<<F<<": "<<to<<endl;
	}
}