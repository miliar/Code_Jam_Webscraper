#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

typedef long long ll;

class pass
{
public:
	ll t;
	ll c;
	ll p;
};

class dinic
{
private:
	ll v, e;

	pass* p;

	vector<pair<ll, ll>>* node;

	ll* jun;

	void bfs()
	{
		queue<ll> q;
		stack<ll> st;
		for (ll i = 0; i < v; i++)
		{
			jun[i] = -1;
		}
		q.push(0);
		jun[0] = 0;
		while (!q.empty())
		{
			ll np = q.front();
			q.pop();
			st.push(np);
			for (int i = 1; i < node[np].size(); i++)
			{
				ll w = node[np][i].second;
				if (p[w].c > 0 && jun[p[w].t] < 0)
				{
					q.push(p[w].t);
					jun[p[w].t] = jun[np] + 1;
				}
			}
		}
		while (!st.empty())
		{
			ll np = st.top();
			st.pop();
			ll mae = 0;
			for (ll i = 1; i < node[np].size(); i++)
			{
				ll w = node[np][i].second;
				if (p[w].c > 0 && jun[p[w].t] == jun[np] + 1 && (p[w].t == v - 1 || node[p[w].t][0].first > 0))
				{
					node[np][mae].first = i;
					mae = i;
				}
			}
			node[np][mae].first = -1;
		}
	}

	pair<bool, ll> dfs(ll n, ll s)
	{
		if (n == v - 1)
		{
			return make_pair(false, s);
		}
		ll mae = 0;
		ll now = node[n][0].first;
		ll all = 0;
		while (now > 0 && s - all > 0)
		{
			ll w = node[n][now].second;
			auto r = dfs(p[w].t, min(p[w].c, s - all));
			p[p[w].p].c += r.second;
			p[w].c -= r.second;
			all += r.second;
			if (p[w].c == 0)
			{
				r.first = true;
			}
			if (r.first)
			{
				node[n][mae].first = node[n][now].first;
			}
			else
			{
				mae = now;
			}
			now = node[n][now].first;
		}
		node[n][mae].first = -1;
		if (mae == 0)
		{
			return make_pair(true, all);
		}
		else
		{
			return make_pair(false, all);
		}
	}
public:
	void set(ll vw, ll ew)
	{
		v = vw;
		p = new pass[ew * 2];
		node = new vector<pair<ll, ll>>[v];
		jun = new ll[v];
		e = 0;
		for (ll i = 0; i < v; i++)
		{
			node[i].push_back(make_pair(0, 0));
		}
	}

	void add(ll f, ll t, ll c)
	{
		p[e].t = t;
		p[e].c = c;
		p[e].p = e + 1;
		p[e + 1].t = f;
		p[e + 1].c = 0;
		p[e + 1].p = e;
		node[f].push_back(make_pair(0, e));
		node[t].push_back(make_pair(0, e + 1));
		e += 2;
	}

	ll solve()
	{
		while (1)
		{
			bfs();
			if (node[0][0].first < 0)
			{
				break;
			}
			dfs(0, ((ll)1 << 50));
		}
		ll all = 0;
		for (int i = 1; i < node[0].size(); i++)
		{
			auto w = node[0][i];
			if (w.second % 2 == 0)
			{
				all += p[p[w.second].p].c;
			}
		}
		return all;
	}

	void del()
	{
		delete[] p;
		delete[] node;
		delete[] jun;
	}
};

char www[100000];
char ww[100000];

int main()
{
	gets(www);
	int t = atoi(www);
	for (int k = 0; k < t; k++)
	{
		map<string, int> mp;
		vector<int> hw[1000];
		int ulas = 0;
		gets(www);
		int n = atoi(www);
		int hh = 0;
		for (int i = 0; i < n; i++)
		{
			gets(www);
			int l = strlen(www);
			int lw = 0;
			for (int j = 0; j < l + 1; j++)
			{
				if ('a' <= www[j] && www[j] <= 'z')
				{
					ww[lw] = www[j];
					lw++;
				}
				else if (lw > 0)
				{
					ww[lw] = '\0';
					if (mp.find(ww) == mp.end())
					{
						mp[ww] = ulas;
						ulas++;
					}
					hw[i].push_back(mp[ww]);
					lw = 0;
					hh++;
				}
			}
		}
		dinic d;
		d.set(n + ulas * 2, hh * 2 + ulas);
		for (int i = 0; i < ulas; i++)
		{
			d.add(n - 1 + i * 2, n - 1 + i * 2 + 1, 1);
		}
		for (auto j : hw[0])
		{
			d.add(0, n - 1 + j * 2, 1);
		}
		for (int i = 2; i < n; i++)
		{
			for (auto j : hw[i])
			{
				d.add(i - 1, n - 1 + j * 2, 1);
				d.add(n - 1 + j * 2 + 1, i - 1, 1);
			}
		}
		for (auto j : hw[1])
		{
			d.add(n - 1 + j * 2 + 1, n + ulas * 2 - 1, 1);
		}
		printf("Case #%d: %lld\n", k + 1, d.solve());
	}
	return 0;
}
