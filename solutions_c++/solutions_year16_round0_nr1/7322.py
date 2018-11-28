#include<iostream>
using namespace std;
int s=0;
void find(long long int n,int a[])
{
	if(n==0)
		return;
	long long int j;
	int k;
	j=n%10;
	for(k=0;k<10;k++)
	{
		if(j==a[k])
		{	a[k]=-1;
			::s++;
		}
	}
	find(n/10,a);
}	

main()
{
	int n,i,j;
	long long int t[100],f;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>t[i];
	}
	for(i=0;i<n;i++)
	{
		int a[10]={0,1,2,3,4,5,6,7,8,9};
		::s=0;
		if(t[i]==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA \n";
		}
		else
		{	
		find(t[i],a);
		j=2;
		f=t[i];
		while(1)
		{
			t[i]=j*f;
			find(t[i],a);
			if(::s==10)
				break;			
			j++;
		}
		cout<<"Case #"<<i+1<<": "<<t[i]<<"\n";
	}}
}
