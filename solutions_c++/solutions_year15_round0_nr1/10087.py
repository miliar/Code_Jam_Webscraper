#include <iostream>
using namespace std;

int main()
{
	int tst;
	cin>>tst;
	for(int k=1;k<=tst;k++)
	{
		int sMax;
		cin>>sMax;
		string a;
		int ar[sMax+1];
		cin>>a;
		for(int i=0;i<=sMax;i++)
		{
			ar[i]=a[i]-'0';
		}
		int sum=ar[0], count=0;
		for(int i=1;i<=sMax;i++)
		{
			if(sum>=i)
			{
				sum+=ar[i];
			}
			else if(ar[i]!=0)
			{
				count=count+i-sum;
				sum=sum+count+ar[i];
			}
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}