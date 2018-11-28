#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>

using namespace std;
int N,M;

const long long MOD = 1000002013;

long long clc(int si,int ei)
{
	long long n = ei-si;
	return (n*N - (n * (n-1))/2)%MOD;

}
#define minn(a,b) ( (a)<(b)? (a) : (b) )
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int TC;
	scanf("%d",&TC);

	for(int tc=1;tc<=TC;tc++)
	{
		cin>>N>>M;
		set<int> s;
		map<long long,long long> m;
		int si,ei,pii;
		long long res = 0;
		long long mx = 0;

		vector< pair<pair<int,int>,int> > ev;
		for(int i=0;i<M;i++)
		{
			cin>>si>>ei>>pii;
			mx+=clc(si,ei)*(pii%MOD);
			mx%=MOD;
			ev.push_back( make_pair(make_pair(si,-1),pii) );
			ev.push_back( make_pair(make_pair(ei,1),pii)  );
			//	m[si] += pii;
		}
		sort(ev.begin(),ev.end());
		for(int i=0;i<ev.size();i++)
		{
			if( ev[i].first.second == -1)
			{
				s.insert(ev[i].first.first);
				m[ev[i].first.first] += ev[i].second;
			}
			else
			{
				while( ev[i].second )
				{
					set<int>::iterator it = s.end();
					it--;
					si = *it;
					long long pi = minn(ev[i].second , m[si] );

					res += clc(si,ev[i].first.first)%MOD * pi%MOD;
					res%=MOD;
					m[si]-= pi;
					if( m[si] <= 0 )
						s.erase( si );

					ev[i].second -= pi;
				}
			}
		}
		cout<<"Case #"<<tc<<": "<<((mx-res)+MOD)%MOD<<endl;
		//printf("Case #%d: %d\n",tc,mx);
	}
	return 0;
}