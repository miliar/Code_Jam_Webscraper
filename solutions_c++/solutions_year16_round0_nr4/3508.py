#include <iostream>
using namespace std;

int main() {
	int t,tt,k,c,s;
	cin>>t;
	tt=t;
	while(tt--)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<t-tt<<":";
		for(int q=1;q<=s;q++)
			cout<<" "<<q;
		cout<<endl;
	}
	return 0;
}