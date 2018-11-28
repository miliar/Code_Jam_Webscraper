#include <iostream>
#include <cstring>
using namespace std;
long long int a[3000],n;

long long int BT(long long int ab[],long long int n1)
{
//	cout<<n1<<endl;
//	cout<<ab[0]<<" "<<ab[1]<<" "<<ab[2]<<" "<<ab[3]<<endl;
	long long int i,max=0,j,x,flag;
	if(n1>1&&ab[0]==ab[n1-1])
	{
		if(a[ab[0]]==ab[1]||a[ab[0]]==ab[n1-2])
		return n1-1;
		else return 0;
	}
	for(i=1;i<=n;i++)
	{
		if(n1<=1||a[ab[n1-1]]==i||a[ab[n1-1]]==ab[n1-2])
		{
			flag=0;
			for(j=1;j<n1;j++)
			{
				if(ab[j]==i)
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				ab[n1]=i;
				x=BT(ab,n1+1);
				if(x>max)
					max=x;
			}
			ab[n1]=0;
		}
	}
	return max;
}

int main() 
{
	long long int t,i,k,x,j,arr[3000];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		for(k=0;k<n;k++)
		{
			cin>>a[k+1];
		}
		cout<<"Case #"<<i+1<<": "<<BT(arr,0)<<endl;
	}
	return 0;
}