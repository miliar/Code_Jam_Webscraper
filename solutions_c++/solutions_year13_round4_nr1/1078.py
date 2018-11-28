#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
using namespace std;
/*struct Node
{
	int O,E,P;
	bool operator <(const Node& t)const
	{
		if(O < t.O)return true;
		else if(O>t.O)return false;
		return E > t.E;
	}
}*/
const long long MOD = 1000002013LL;
long long f(long long N,long long x)
{
	return ((2*N+1-x)*x/2)%MOD;
}
long long O[1010];
long long E[1010];
long long P[1010];
int main()
{
	int T,Cidx=0;
	cin >> T;
	while(T--)
	{
		++Cidx;
		int N,M;
		cin >> N >> M;
		map<int,int>toNew;
		map<int,int>toOld;
		map<long long,long long>begin;
		map<long long,long long>end;
		map<long long,long long>Total;
		set<int>Num;
		long long rans =0;
		for(int i=0;i<M;++i)
		{
			cin >> O[i] >> E[i] >> P[i];
			Num.insert(O[i]);
			Num.insert(E[i]);
			begin[O[i]] += P[i];
			end[E[i]] += P[i];
			Total[O[i]]+=P[i];
			Total[E[i]]+=P[i];
		}
		for(int i=0;i<M;++i)
			rans = (rans + f(N,E[i]-O[i])*P[i]%MOD)%MOD;
		long long bans  = 0;
		vector<pair<long long ,long long > > curr;
		for(map<long long,long long>::iterator itr = Total.begin();itr!=Total.end();++itr)
		{
			if(begin.find(itr->first)!=begin.end())
				curr.push_back(make_pair(itr->first,begin[itr->first]));
			if(end.find(itr->first)!=end.end())
			{
				long long tend = end[itr->first];
				for(int i=curr.size()-1;i>=0;--i)
				{
					long long used = min(curr[i].second,tend);
					tend -= used;
					curr[i].second -= used;
					bans += f(N,itr->first - curr[i].first)%MOD*used%MOD;
					if(curr[i].second==0)
							curr.pop_back();
					if(tend == 0)break;
				}
			}
		}
		cout << "Case #"<<Cidx<<": "<<(rans+MOD-bans)%MOD<<endl;
	}
	return 0;
}
