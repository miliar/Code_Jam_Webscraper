#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int a, b, k, count=0;
		cin>>a;
		cin>>b;
		cin>>k;
		for(int j=0;j<a;j++)
		{
			for(int l=0;l<b;l++)
			{
				if((j&l)<k)
					count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
