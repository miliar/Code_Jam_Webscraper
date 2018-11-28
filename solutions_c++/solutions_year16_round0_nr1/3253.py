#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
	long long int cases,caseno=1;
	cin>>cases;
	while(cases--)
	{
		long long int n,count=0,a[10]={0};
	cin>>n;
	if(n==0)
	{
		cout << "Case #" << caseno++ << ": " << "INSOMNIA\n";
		continue;
	}
	long long int i=1;
	while(count!=10)
	{
		long long int temp=n*i++;
		while(temp!=0)
		{
			long long int x=temp%10;
			if(a[x]==0)
			{
				count++;
				a[x]++;
			}
			temp=temp/10;
		}
	}
	cout << "Case #" << caseno++ << ": " << n*(i-1) << "\n";
	}
	return 0;
}
