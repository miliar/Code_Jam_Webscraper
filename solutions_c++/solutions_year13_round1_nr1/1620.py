#include<iostream>
#include<fstream>
using namespace std;


long tot(int r,int t)
{
	long ans=0;
	long a=1;
	while(t-2*r-a>=0)
	{
		t=t-2*r-a;
		//cout<<a;
		ans++;
		a=a+4;
	}
	
	return ans;
}




int main()
{
	
	freopen("A.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int test;
	int r,t;
	
	long ans=0;
	int q=1;
	
	cin>>test;
	
	while(test--)
	{
		cin>>r>>t;
		
		
		cout<<"Case #"<<q<<": "<< tot(r,t)<<endl;
		q++;
	}
	
}
