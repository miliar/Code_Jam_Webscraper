#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	scanf("%d",&n);
	int r=1;
	while(n--)
	{
		
		int x;
		char arr[1001];
		cin>>x;
		cin>>arr;
		int count=0,k=0,sum=0;
		sum=sum+arr[0]-48;
		for(int i=1;i<strlen(arr);i++)
		{
		//	cout<<sum<<"  "<<i<<" "<<count<<endl;
		    if(sum<i)
		    {
		    	count++;
		    	sum++;
		    }
		    sum=sum+arr[i]-48;
		}
		cout<<"Case #"<<r<<": "<<count<<endl;
		r++;
	}
	return 0;
}
