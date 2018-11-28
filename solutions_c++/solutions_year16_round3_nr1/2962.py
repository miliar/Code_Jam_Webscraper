#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
struct idea
{
	int i,x; 
};
bool cmp(idea a,idea b)
{
	return a.x>b.x;
}
int main(void)
{
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		int n,sum=0;
		cin>>n;
		
		idea arr[27];
		for(int i=0;i<n;i++)
			{
				cin>>arr[i].x;
				arr[i].i=i;
				sum+=arr[i].x;
			}		
		cout<<"Case #"<<l<<": ";
		sort(arr,arr+n,cmp);
		while(arr[0].x!=0)
		{
			sum-=1;

			if(arr[1].x>sum/2)
			{
				arr[0].x-=1;
				arr[1].x-=1;
				sum-=1;
				cout<<(char)(arr[0].i+'A')<<(char)(arr[1].i+'A')<<" ";
			}
			else
			{
				arr[0].x-=1;
				cout<<(char)(arr[0].i+'A')<<" ";
			}
			sort(arr,arr+n,cmp);

		}
		cout<<endl;

	}
}