#include<iostream>
using namespace std;
int main()
{
	int t,k,c,s;
	cin>>t;
	int m =1;
	while(t--)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<m++<<":";
		for(int i=1 ; i<k+1;i++)
		{
			cout<<" "<<i;
		}
		cout<<endl;
	}

	return 0;
}