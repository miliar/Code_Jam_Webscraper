#include <iostream>

using namespace std;

int main()	{
	long long t,k,c,s,cases,i;
	cin>>t;
	cases = 0;
	while(t--)	{
		cases++;	//to count the cases
		cin>>k>>c>>s;
		cout<<"Case #"<<cases<<": ";
		for(i=1;i<=k;i++)	cout<<i<<" ";
		cout<<endl;
	}
}