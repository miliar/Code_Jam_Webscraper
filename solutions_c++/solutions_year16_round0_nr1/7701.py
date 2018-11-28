#include <iostream>
#include <set>
using namespace std;
int main(int argc, char const *argv[])
{
	long long int t,n;
	cin>>t;
	
 	set<int>::iterator it;
 	int test=1;
	while(test!=t+1)
	{
		set<int> myset;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<test<<": INSOMNIA\n";
		else
		{
			long long int f=1;
			long long int temp=n;
			while(myset.size()!=10)
			{
				long long int y=n;
				while(y!=0)
				{
					myset.insert(y%10);
					y=y/10;
				}
				f++;
				n=f*temp;
			}
			cout<<"Case #"<<test<<": "<<n-temp<<"\n";
			
		}
		test++;
	}
	return 0;
}