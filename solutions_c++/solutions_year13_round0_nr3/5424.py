#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int a,b;
		int ans=0;
		cin>>a>>b;
		if(a==1)  ans++;
		if(a<=4 && b>=4) ans++;
		if(a<=9 && b>=9) ans++;
		if(a<=121 && b>=121) ans++;
		if(a<=484 && b>=484) ans++;
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}