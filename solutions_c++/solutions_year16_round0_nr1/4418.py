#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	unsigned long long t,k=0,num,x,temp,i,ans;
	cin>>t;
	while(t--)
	{
		ans=0;
		set<int> s;
		cin>>num;
		if(num==0)
		{
			cout<<"Case #"<<++k<<": INSOMNIA"<<"\n";
			continue;
		}
		i=1;
		while(s.size()!=10)
		{
			temp=num*i;
			i++;
			while(temp)
			{
				x=temp%10;
				temp/=10;
				s.insert(x);
			}
			ans++;
		}
		cout<<"Case #"<<++k<<": "<<(long long)num*ans<<"\n";
	}
}