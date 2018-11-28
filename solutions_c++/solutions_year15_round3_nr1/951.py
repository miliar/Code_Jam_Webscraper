#include <iostream>
using namespace std;

int main() {
	// t r c w
	
	int t,r,c,w;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>r>>c>>w;
		int a=c/w*r+w;
		if (c%w==0)
		a--;
		cout<<a<<endl;
	}
	return 0;
}