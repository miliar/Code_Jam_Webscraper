#include <iostream>
using namespace std;


int main()
{
	int t=0,k,c,s;
	

	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		cin>>k;
		cin>>c;
		cin>>s;	
		
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<k;j++)
			cout<<j+1<<" ";
		cout<<endl;
	}
	
	
		return 0;
}		