#include<iostream>
using namespace std;
int main()
{
	int c=1;
	int arr[10];
	arr[1]=1;
	arr[2]=4;
	arr[3]=9;
	arr[4]=121;
	arr[5]=484;
	int t;
	int count=0;
	int a,b;
	cin>>t;
	while(t--)
	{
		count=0;
		cin>>a>>b;
		for(int i=0;i<=5;i++)
		{
			if(arr[i]>=a && arr[i]<=b)
				count++; 
		}
		cout<<"Case #"<<c<<": "<<count<<endl;
		c++;
	}
	return 0;
}
