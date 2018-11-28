#include<bits/stdc++.h>
using namespace std;

int main()
{
	#ifdef DBG
	freopen("A-large.in", "r" , stdin);
	freopen("A-large.out", "w" , stdout);
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T,c=1,L;
	string str;
	cin>>T;
	while(T--)
	{
		cin>>L>>str;
		int ans = 0;
		int sum = 0;
		for(int i=0;i<=L;++i)
		{
			int p = str[i]-'0';
			if( sum<i ){
				ans +=i-sum;
				sum=i;
			}
			sum+=p;
		}
		cout<<"Case #"<<c++<<": "<<ans<<'\n';
	}

}

