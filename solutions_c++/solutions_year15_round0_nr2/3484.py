#include <bits/stdc++.h>
using namespace std;
int T,TT,D;
int main()
{
	TT=0;
	cin>>T;
	while(T--)
	{
		cin>>D;
		vector<int> v;
		int ma=0;
		for(int i=0;i<D;i++)
		{
			int P;
			cin>>P;
			ma=max(ma,P);
			v.push_back(P);
		}
		if(ma<4)
		{
			TT++;
			cout<<"Case #"<<TT<<": ";
			cout<<ma<<endl;
			continue;
		}
		int u=1000;
		for(int x=1;x<=1000;x++)
		{
			int uu=0;
			for(int i=0;i<D;i++)
			{
				if(v[i]>x)
				{
					uu+=((v[i]-1)/x);
				}
			}
			u=min(u,uu+x);
		}
		TT++;
		cout<<"Case #"<<TT<<": ";
		cout<<u<<endl;
	}
	return 0;
}