#include <iostream>
using namespace std;

int max(int a,int b)
{
	if (a>b)
		return a;
	else
	return b;
}
int min(int a,int b)
{
	if (a>b)
		return b;
	else
	return a;
}

int a[1005];

int main() {
	int test,cas;
	cin>>test;
	for(cas=1;cas<=test;cas++)
	{
	int n,max_elem=-1,max_time,i,div,j;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
		if(a[i]>max_elem)
			max_elem=a[i];
	}
	max_time=max_elem;
	for(i=1;i<=max_elem;i++)
	{
		div=i;
		for(j=0;j<n;j++)
		{
			if(a[j]>i)
			{
				if(a[j]%i==0)
					div+=((a[j]/i)-1);
				else
					div+=(a[j]/i);
			}
			
		}
		if(div<max_time)
				max_time=div;
	}
	cout<<"Case #"<<cas<<": "<<max_time<<endl;
	}
	return 0;
}