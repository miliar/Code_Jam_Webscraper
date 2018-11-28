#include<bits/stdc++.h>
using namespace std;
string make_string(int in)
{
	int j=0;
	int icopy=in;
	while(icopy)
	{
		icopy/=2;
		j++;
	}
	string ret;
	ret.resize(2*j);
	//cout<<j<<endl;
	for(int i=0;i<j;++i)
	{
		ret[j-1-i]=char(in%2+48);
		ret[j-1+i+1]=char(in%2+48);
		in/=2;
	}
	return ret;
}
int main()
{
	int	test;
	cin>>test;
	while(test--)
	{
		int n,j;
		cin>>n>>j;
		int L;
		if(n%2==0)
		{
			L=int(pow(2.0,n/2.0-1));
		}
		cout<<"Case #1:\n";
		for(int i=0;i<j;++i)
		{
			cout<<make_string(L+i)<<" 3 2 5 2 7 2 3 5 11\n";
		}
		
	}
	
	return 0;
}
