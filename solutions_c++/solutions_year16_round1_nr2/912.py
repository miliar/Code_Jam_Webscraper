#include<iostream>
#include<algorithm>
using namespace std;
int arr[10000];
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		int freq[3000]={0};
		int n,pos=0;
		cin>>n;
		for(int i=0;i<n*(2*n-1);i++)
		{
			int x;
			cin>>x;
			//cout<<"got "<<x<<endl;
			freq[x]=(freq[x]+1)%2;
		}
		for(int i=0;i<3000;i++)
		{
			if(freq[i]>0)
			{
				arr[pos]=i;
				pos++;
			}
		}
		if(pos<n)
		{
			cout<<"error-----------------";
		}
		sort(arr,arr+pos);
		cout<<"Case #"<<tt<<": ";
		for(int i=0;i<n;i++)
		{
			cout<<arr[i]<<" ";
		}
		cout<<endl;
	}
	
}
