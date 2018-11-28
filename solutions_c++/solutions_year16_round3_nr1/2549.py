#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		int n;
		cin>>n;
		int p[n];
		int sum=0;
		int ch=0;
		int max=p[0];
		char s;
		for(int j=0;j<n;j++)
		{
			cin>>p[j];
			sum=sum+p[j];
		}
		for(int j=0;j<sum;j++)
		{
			for(int k=0;k<n;k++)
			{
				if(p[k]>max)
				{
					max=p[k];
					ch=k;
				}
			}
			p[ch]=p[ch]-1;
			if(j%2==0 && j<sum-2 && j>0)
				cout<<" ";
			if(j==sum-2 && j>0)
				cout<<" ";
			s=(char)(int)65+ch;
			cout<<s;
			max=p[0];
			ch=0;
		}
		cout<<endl;
	}
}