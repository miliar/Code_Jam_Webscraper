#include <bits/stdc++.h>
using namespace std;

int main() {
	long long n,i,j,t,ans=0,sz=1;
	set<int> x;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		sz=1;
		if(n!=0)
		{
			ans=0;
			while(sz!=10)
			{
				ans+=n;
				j=ans;
				while(j)
				{
					x.insert(j%10);
					j/=10;
				}
				sz=x.size();
			}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		} else cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		x.clear();
	}
	return 0;
}