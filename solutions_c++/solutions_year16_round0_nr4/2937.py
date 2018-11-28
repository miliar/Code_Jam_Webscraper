#include <iostream>
using namespace std;

int main() {
long long int t,i,k,c,s,j;
cin>>t;
for(i=0;i<=t;i++)
{
	cin>>k>>c>>s;
	 cout<<"Case #"<<i<<":";
	for(j=1;j<=k;j++)
	{
		cout<<" "<<j;
	}
	cout<<"\n";
}
	return 0;
}