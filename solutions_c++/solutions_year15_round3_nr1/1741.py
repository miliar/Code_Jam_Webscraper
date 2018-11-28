#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int r,c,w;
		cin>>r>>c>>w;
		int res=(c-w+1)/2+w;
		int count1=0;
		while(c-w>=w)
		{
			c=c-w;
			count1++;
		}
		if(c<=w)
		{
			count1=count1+w;
		}
		else
		{
			count1=count1+1+w;
		}


		cout<<"Case #"<<i<<": "<<count1<<endl;
	}
}