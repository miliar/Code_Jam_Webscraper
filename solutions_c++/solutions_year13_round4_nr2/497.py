#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
typedef long long ll;

struct seg
{
	ll b,e,v;
	seg(ll b,ll e,ll v):b(b),e(e),v(v) {}
};

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int E; ll P;
		cin>>E>>P;
		const ll N=1LL<<E;
		ll Q1=0,Q2=N-1; vector<seg> V1,V2;
		V1.push_back(seg(Q1,Q1,1));
		V2.push_back(seg(Q2,Q2,N));
		Q1++;
		Q2--;
		for(int j=0;j<E;j++)
		{
			const ll num=1LL<<(E-j-1);
			const ll dif=(2LL<<j)-1;
			V1.push_back(seg(Q1,Q1+num-1,1+dif));
			V2.push_back(seg(Q2-num+1,Q2,N-dif));
			Q1+=num;
			Q2-=num;
		}
		ll A1=0,A2=0;
		for(int j=0;j<V1.size();j++)
		{
			for(int k=0;k<V2.size();k++)
			{
				const ll b=max(V1[j].b,V2[k].b);
				const ll e=min(V1[j].e,V2[k].e);
				if(b>e)continue;
				if(V2[k].v<=P)A1=max(A1,e);
				if(V1[j].v<=P)A2=max(A2,e);
			}
		}
		cout<<"Case #"<<i<<": "<<A1<<' '<<A2<<endl;
	}
	return 0;
}
