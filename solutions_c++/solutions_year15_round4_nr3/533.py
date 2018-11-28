#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define fre 	freopen("0.in","r",stdin),freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
#define lld signed long long int
#define pp pop_back()
#define ps(x) push_back(x)
#define mpa make_pair
#define pii pair<int,int>
#define fi first
#define se second
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define boost ios_base::sync_with_stdio(0)
//vector<int> g[2*100000+5];int par[2*100000+5];
double V,X;
double v[6654],c[6464];
vector<string> token(string S)
{
	vector<string>ans;
	ans.clear();

	for(int i=0;i<S.size();)
	{
		string temp="";

		while(S[i]!=' ' and i<S.size())
			temp+=S[i],++i;
		++i;
		while(S[i]==' ' and i<S.size())
			++i;
		ans.ps(temp);
	}
	return ans;
}
vector<string>E,F,temp;
map<string,int>mp;
int l1[1000000+5];
int l2[1000000+5];
int TL1[1000000+5];
int TL2[1000000+5];
vector<int>G[1000000+5];
int main()
{
	fre;
	int N,T;
	cin >> T;
	for(int t=1;t<=T;++t)
	{
		int N;
		cin>>N;
		cin.ignore();

		int p =0;
		mp.clear();

		string S;
		std::getline (std::cin,S);
		E = token(S);
		std::getline (std::cin,S);
		F = token(S);
		for(int i=0;i<E.size();++i)
		{
			if(mp[E[i]]==0)
				mp[E[i]] = ++p;
			l1[mp[E[i]]] = 1;
		}
		for(int i=0;i<F.size();++i)
		{
			if(mp[F[i]]==0)
				mp[F[i]] = ++p;
			l2[mp[F[i]]] = 1;
		}
		for(int i=3;i<=N;++i)
		{
			std::getline (std::cin,S);
			temp = token(S);
			G[i-2].clear();
			for(int j=0;j<temp.size();++j)
			{
				if(mp[temp[j]]==0)
					mp[temp[j]] = ++p;
				G[i-2].ps(mp[temp[j]]);
			}
		}
		int ans=MOD;
		for(int mask=0;mask<(1<<(N-2));++mask)
		{
			for(int i=0;i<=p;++i)
				TL1[i] = (l1[i]==1),
				TL2[i] = (l2[i]==1);
			for(int i=0;i<N-2;++i)
			{
				if(mask & (1LL<<i))
				{
					for(int j=0;j<G[i+1].size();++j)
						TL1[G[i+1][j]] = 1;
				}
				else
				{
					for(int j=0;j<G[i+1].size();++j)
						TL2[G[i+1][j]] = 1;
				}
			}
			int g =0;
			for(int i=1;i<=p;++i)
			{
				if(TL1[i] and TL2[i])
					++g;
			}
			ans=min(ans,g);
		}
		printf("Case #%d: %d\n",t,ans);
		for(int i=0;i<=p;++i)
		{
			TL1[i]=0;
			TL2[i]=0;
			l1[i]=0;
			l2[i]=0;
		}
	}
}
