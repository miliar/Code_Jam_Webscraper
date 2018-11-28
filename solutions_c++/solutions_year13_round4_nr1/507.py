#include<algorithm>
#include<iostream>
#include<map>
#include<vector>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;

int N; ll C1,C2;
map<int,int> BST;
vector<PII> V;

void solve()
{
	map<int,int>::const_iterator it;
	for(it=BST.begin();it!=BST.end();++it)
	{
		const int t=it->first>>1;
		const int z=it->first& 1;
		int p=it->second;
		if(z==0)
		{
			V.push_back(PII(t,p));
			continue;
		}
		while(p>0)
		{
			const int u=min(p,V.back().second);
			const int d=t-V.back().first;
			C2+=u*((ll)d*N-(ll)d*(d-1)/2);
			p-=u;
			if((V.back().second-=u)==0)V.pop_back();
		}
	}
}

void input()
{
	C1=0;
	C2=0;
	BST.clear();

	int m;
	cin>>N>>m;
	while(m-->0)
	{
		int o,e,p;
		cin>>o>>e>>p;
		if(p<=0)continue;
		const int d=e-o;
		C1+=p*((ll)d*N-(ll)d*(d-1)/2);
		BST[o<<1]+=p;
		BST[(e<<1)|1]+=p;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		input();
		solve();
		cout<<"Case #"<<i<<": "<<C1-C2<<endl;
	}
	return 0;
}
