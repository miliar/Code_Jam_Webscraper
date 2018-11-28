#include<iostream>
using namespace std;
int main()
{
	int t;
	long long a,b,c,count=0,ix=0;
	cin>>t;
	while(t>0)
	{ ix++;
	 count=0;
		cin>>a>>b>>c;
		
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<c)
				{
					count++;
					//cout<<i<<" "<<j;
				}
			}
		}
		
		cout<<"Case #"<<ix<<": "<<count<<endl;
		t--;
	}
	
	
}
