#include<iostream>
using namespace std;
int main()
{
	int ctr=0;
	int arr[10];
	for(int i=0;i<10;i++)
	{
		arr[i]=-1;
	}
	long t,*n;
	cin>>t;
	n=new long[t];
	for(int i=0;i<t;i++)
	{
		ctr=0;
		cin>>n[i];
		if(n[i]==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else
		{
			int j=1;
			int temp=n[i];
			while(ctr!=10)
			{
				temp=n[i]*j;
				while(temp>0)
				{
					int k=temp%10;
					int flag=0;
					for(int c=0;c<ctr;c++)
					{
						if(arr[c]==k)
						{
							flag=1;
						}
					}
					if(flag==0)
					{
						arr[ctr]=k;
						
						ctr++;
					}
					temp/=10;
					
				 }	
				 j++;								
			}
			cout<<"Case #"<<i+1<<": "<<(j-1)*n[i]<<endl;
		}
	}
	return 0;
}
