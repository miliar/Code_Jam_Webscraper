#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

const long long MOD = 1000002013;
struct Data
{
	int e, p;
	bool operator < (const Data& a)const {return e == a.e ? p > a.p : e < a.e;}
};
long long fee(long long n, long long dist)
{
	return (n*dist-dist*(dist-1)/2)%MOD;
}
int main()
{
	int T;
	cin>>T;
	for(int _=1;_<=T;_++)
	{
		int n, m;
		cin>>n>>m;
		vector<Data> event(2*m);
		long long result = 0;
		for(int i=0;i<m;i++)
		{
			int o, e, p;
			cin>>o>>e>>p;
			event[2*i].e = o;
			event[2*i].p = p;
			event[2*i+1].e = e;
			event[2*i+1].p = -p;
			result += fee(n, e-o) * p;
			result %= MOD;
		}
		sort(event.begin(), event.end());
		vector<Data> q;
		q.reserve(2*m);
		for(int i=0;i<event.size();i++)
			if(event[i].p > 0)
				q.push_back(event[i]);
			else
			{
				for(int p = -event[i].p, j = q.size()-1; p>0; j--)
				{
					if(j < 0) cerr<<"PANIC!"<<endl;
					int t = min(p, q[j].p);
					result -= fee(n, event[i].e-q[j].e) * t;
					result %= MOD;
					p -= t;
					q[j].p -= t;
					if(0 == q[j].p)
						q.resize(j);
				}
			}
		result += MOD;
		result %= MOD;
		cout<<"Case #"<<_<<": "<<result<<endl;
	}
	return 0;
}
