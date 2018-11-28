#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int a,b,k;
		cin>>a>>b>>k;
		int cnt = 0 ;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if( (i&j) < k ) cnt ++;
			}
		}
		cout<<"Case #"<<tc<<": "<<cnt<<"\n";
	}
	
	return 0;
}
