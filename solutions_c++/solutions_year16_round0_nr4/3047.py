#include <iostream>
using namespace std;

int main() {
	int t,T,a,b,c,i;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>a>>b>>c;
		if(a!=c)
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else
		{
			cout<<"Case #"<<t<<": ";
			for(i=1;i<=a;i++)
			{
				cout<<i<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}