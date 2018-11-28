#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<stack>
using namespace std;

struct event
{
	long long kind,x,num;
	event(){}

	bool operator <(const event &a)const
	{
		if(x != a.x)
			return x < a.x;
		return kind < a.kind;
	}
};
event make(long long a,long long b,long long c)
{
	event t;
	t.kind = a;
	t.x = b;
	t.num = c;
	return t;
}
long long N;
#define mod 1000002013

long long cnt(long long c)
{
	return ((c * (c + 1)) / 2) % mod;
}

long long from(long long a,long long b)
{
	return (cnt(N) - cnt(N - (b - a)) + mod) % mod;
}

int main()
{
	freopen("text.txt","r",stdin);
	freopen("sol.txt","w",stdout);
	long long T,M;
	cin >> T;
	for(long long TEST = 1 ; TEST <= T; TEST++)
	{
		vector<event> ev;
		cin >> N >> M;
		long long ans1 = 0;
		for(long long i = 0 ; i < M; i++)
		{
			long long a,b,p;
			cin >> a >> b >> p;
			ans1 += (from(a,b) * p) % mod;
			ans1 %= mod;
			ev.push_back(make(0,a,p));
			ev.push_back(make(1,b,p));
		}
		sort(ev.begin(),ev.end());
		stack<pair<long long,long long> > S;
		long long ans = 0;
		for(long long i = 0; i < (long long)ev.size(); i++)
		{
			if(ev[i].kind == 0)
				S.push(make_pair(ev[i].x,ev[i].num));
			else
			{
				long long r = ev[i].num;
				while(1)
				{
					pair<long long,long long> t = S.top();
					S.pop();
					if(r > t.second)
					{
						ans += (from(t.first,ev[i].x) * t.second) % mod;
						ans %= mod;
						r -= t.second;
					}
					else
					{
						ans += (from(t.first,ev[i].x) * r) % mod;
						ans %= mod;
						t.second -= r;
						S.push(t);
						break;
					}
				}
			}
		}
		cout << "Case #"<<TEST<<": " << (ans1 - ans + mod) % mod << endl;
	}
}
