#include<iostream>

using namespace std;

int main()
{
	int t,k,c,s,count,i=1,j;
	cin>>t;
	while(t-- > 0)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<i<<":";
		if(k==1 || c==1)
			count=k;
		else
			count=k-1;
		if(count<=s)
		{
				for(j=k;count>0;--j,--count)
					cout<<" "<<j;
		}
		else
			cout<<" IMPOSSIBLE";
		cout<<endl;
		++i;
	}
	return 0;
}