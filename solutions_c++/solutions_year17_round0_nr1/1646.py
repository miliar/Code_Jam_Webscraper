#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T,N,K; cin>>T;
	string s;
	for (int t=1;t<=T;t++)
	{
		cin>>s>>K;
		N=s.size();
		int r=0;
		for (int i=0;i<=N-K;i++)
		{
			if (s[i]=='-')
			{
				r++;
				for (int j=i;j<i+K;j++)
					s[j]=(s[j]=='+'?'-':'+');
			}
		}
		bool f=true;
		for (int i=N-K+1;i<N;i++)
			if (s[i]=='-') {f=false; break;}
		cout<<"Case #"<<t<<": ";
		if (f) cout<<r<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}