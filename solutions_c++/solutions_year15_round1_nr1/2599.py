#include <iostream>
using namespace std;
int main()
{
	int test,n,max_c,diff,arr[1000];
	unsigned int min_1,min_2;
	cin>>test;
	for(int j=1;j<=test;j++)
	{
		cin>>n;
		for(int z=0; z<n; z++)
			cin>>arr[z];
		min_1=max_c=0;
		for(int z=0; z<n-1; z++)
		{
			diff=arr[z]-arr[z+1];
			if(diff>0)
				min_1+=diff;
		}
		for(int z=0; z<n-1; z++)
		{
			diff=arr[z]-arr[z+1];
			if(diff>max_c)
				max_c=diff;
		}
		min_2=0;
		for(int z=0; z<n-1; z++)
		{
			if(arr[z]>max_c)
				min_2=min_2+max_c;
			else
				min_2=min_2+arr[z];
		}
		cout<<"Case #"<<j<<": "<<min_1<<" "<<min_2<<endl;
	}
	return 0;
}
