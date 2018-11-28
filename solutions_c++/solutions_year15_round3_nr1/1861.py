#include<iostream>
using namespace std;
int main()
{
	int t,r,c,w,i=0;
	cin>>t;
	while(t--)
	{
		i++;
		cin>>r>>c>>w;
		cout<<"Case #"<<i<<": ";
		//if(c>w)
		if(!(c%w))
		cout<<r*(c/w + w -1)<<endl;
		else
			cout<<r*(c/w + w)<<endl;
		//else
		//	cout<<w<<endl;
	}
	return 0;
}
