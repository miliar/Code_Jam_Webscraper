#include<iostream>
using namespace std;
int main()
{
	int t,te,ans=0,a,b;
	cin>>t;
	for(te=0;te<t;te++)
	{
		cin>>a>>b;
		ans=0;
		if(b>=1)
			ans++;
		if(b>=4)
			ans++;
		if(b>=9)
			ans++;
		if(b>=121)
			ans++;
		if(b>=484)
			ans++;
		if(a>1)
			ans--;
		if(a>4)
			ans--;
		if(a>9)
			ans--;
		if(a>121)
			ans--;
		if(a>484)
			ans--;
		cout<<"Case #"<<te+1<<": "<<ans<<"\n";		
	}
	return 0;
}
