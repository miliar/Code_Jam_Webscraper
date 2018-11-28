#include <bits/stdc++.h>
using namespace std;
int k,c,s;
long long find_next(long long a,long long b,long long len)
{
	//cout<<a<<' '<<b<<' '<<(a-1)*len+b<<endl;
	return (a-1)*len+b;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T,no=0;
	cin>>T;
	while(T--)
	{
		cin>>k>>c>>s;
		vector<long long> ori,tmp;
		for(int i=1;i<=k;i++) ori.push_back(i);
		long long len=k;
		for(int i=2;i<=c;i++)
		{
			tmp.clear();
			if(ori.size()%2!=0) ori.push_back(ori.back());
			for(int i=1;i<(int)ori.size();i+=2)
				tmp.push_back(find_next(ori[i-1],ori[i],len));
			len*=k;
			tmp.swap(ori);
		}
		if((int)ori.size()<=s)
		{
			cout<<"Case #"<<++no<<":";
			for(int i=0;i<(int)ori.size();i++)
				cout<<' '<<ori[i];
			cout<<'\n';
		}
		else
		{
			cout<<"Case #"<<++no<<": IMPOSSIBLE\n";
		}
	}
}