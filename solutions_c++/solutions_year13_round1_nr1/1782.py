#include <iostream>

using namespace std;

int main()
{
	long long T,r;
	long long t;
	cin>>T;
	for(int i=0; i<T; i++)
	{
		long long c=0;
		long long plus=0;
		cin >> r >> t ;
		while(t>=0)
		{
			
			t=t-(r+(r+1)+plus);
			if(t>=0)
				c++;
			plus+=4;
		}
		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}
}