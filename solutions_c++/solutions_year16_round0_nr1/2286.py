#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,t,T;
	cin>>t;
	T=t;
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<T-t<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int arr[10]={0,0,0,0,0,0,0,0,0,0};
		int j=1;
		while(1)
		{
			long long int m=j*n;
			long long int temp2=m;	
			while(m>0)
			{
				int temp=m%10;
				arr[temp]=1;
				m=m/10;	
			}
			int flag;
			for(int ss=0;ss<10;ss++)
			{
				flag=1;
				if(arr[ss]==0)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)
			{
				cout<<"Case #"<<T-t<<": "<<temp2<<endl;
				break;
			}
			j++;	
		}	
	}
	return 0;
}
