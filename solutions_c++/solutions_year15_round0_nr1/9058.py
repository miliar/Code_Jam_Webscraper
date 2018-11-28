#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int s[10000],smax,tmp,sum;
	string c;
	for(int i=1;i<=t;i++)
	{
		cin>>smax;
		tmp=0;sum=0;
		cin>>c;
		for(int j=0;j<=smax;j++)
			s[j]=c[j]-'0';
		sum=s[0];
		for(int j=1;j<=smax;j++)
		{
			if(sum<j)
			{
				tmp+=j-sum;
				sum=j;
			}
			sum+=s[j];
		}
		cout<<"Case #"<<i<<": "<<tmp<<endl;
	}
	return 0;
}
