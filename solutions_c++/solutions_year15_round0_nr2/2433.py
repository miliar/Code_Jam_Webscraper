#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<math.h>
using namespace std;

int main()
{
	int n;
	cin>>n;
	int arr[2000];
	int z=0;
	int min[1010];
int i,j,m,k,sum=0;
for (i = 0; i < n; i++)
{
	cin>>m;
	for (j = 0; j < m; j++)
	{
		cin>>arr[j];
	}
	sort(arr,arr+m);
	z= arr[m-1];
	for (j = 1; j < z+1; j++)
	{
		sum=0;
		for (k = 0; k <m ; k++)
		{
			sum += ceil((double)arr[k]/j)-1;
		}
		sum = sum + j;
		min[j-1]=sum;
	}
	sort(min,min+z);
	cout<<"Case #"<<i+1<<": "<<min[0]<<"\n";
	

}




}
