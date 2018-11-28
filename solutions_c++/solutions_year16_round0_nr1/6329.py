#include<iostream>
using namespace std;
int is(int a[])
{
	int i;
	for(i=0;i<=9;i++)
		if(!a[i])
			break;
	if(i==10)
		return 1;
	return 0;
}
int main()
{
	int t,i,n,a[10],j,k,temp,out;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		for(j=0;j<=9;j++)
			a[j]=0;
		cin>>n;
		k=1;
		cout<<"Case #"<<i<<": ";
		if(n!=0)
		{
			while(1)
			{
				
				
				temp=n*k;
				//cout<<temp<<"\t";
				out=temp;
				k++;
				while(temp>0)
				{
					a[temp%10]=1;
					temp=temp/10;
				}
				if(is(a))
					break;
			}
		cout<<out<<endl;
		}
		else
		cout<<"INSOMNIA"<<endl;
	}
	return 0;
}