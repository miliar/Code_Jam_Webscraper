#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>

using namespace std;

typedef long long ll;

ll n, d;

vector<ll> k[2000000];
ll o[2000000];
ll s[2000000];
bool nowo[2000000];

priority_queue<pair<ll, ll>> pq1;
priority_queue<pair<ll, ll>> pq2;

void dfsm(ll now)
{
	for (auto i : k[now])
	{
		dfsm(i);
	}
	nowo[now] = false;
}

ll dfs1(ll now)
{
	if (s[0] <= s[now] && s[now] <= s[0] + d)
	{
		ll all = 1;
		for (auto i : k[now])
		{
			all += dfs1(i);
		}
		nowo[now] = true;
		if (s[0] < s[now])
		{
			pq1.push(make_pair(s[now], now));
		}
		return all;
	}
	else 
	{
		if (s[now] < s[0])
		{
			pq2.push(make_pair(s[now], now));
		}
		dfsm(now);
		return 0;
	}
}

ll dfsm2(ll now)
{
	if (nowo[now])
	{
		ll all = 1;
		for (auto i : k[now])
		{
			all += dfsm2(i);
		}
		nowo[now] = false;
		return all;
	}
	else
	{
		return 0;
	}
}

ll dfs2(ll now, ll ok)
{
	if (ok - d <= s[now] && s[now] <= ok)
	{
		ll all = 1;
		for (auto i : k[now])
		{
			all += dfs2(i, ok);
		}
		nowo[now] = true;
		if (s[0] < s[now])
		{
			pq1.push(make_pair(s[now], now));
		}
		return all;
	}
	else
	{
		if (s[now] < s[0])
		{
			pq2.push(make_pair(s[now], now));
		}
		return 0;
	}
}

ll ww[2000000];

int main()
{
	ll t;
	scanf("%lld", &t);
	for (ll tw = 0; tw < t; tw++)
	{
		scanf("%lld%lld", &n, &d);
		for (ll i = 0; i < n; i++)
		{
			k[i].clear();
		}
		ll w1, w2, w3, w4;
		scanf("%lld%lld%lld%lld", &w1, &w2, &w3, &w4);
		ll q1, q2, q3, q4;
		scanf("%lld%lld%lld%lld", &q1, &q2, &q3, &q4);
		ll nowkk = 0;
		for (ll i = 0; i < n; i++)
		{
			s[i] = w1;
			if (i == 0 || s[i] > s[0])
			{
				ww[nowkk] = s[i];
				nowkk++;
			}
			w1 = (w1 * w2 + w3) % w4;
			if (i > 0)
			{
				o[i] = q1 % i;
				k[q1 % i].push_back(i);
			}
			q1 = (q1 * q2 + q3) % q4;
		}
		sort(ww, ww + nowkk, greater<ll>());
		ll nowk = dfs1(0);
		ll maxw = nowk;
		bool fir = true;
		for (int i = 0; i < nowkk; i++)
		{
			ll w = 0;
			while (1)
			{
				if (pq1.empty())
				{
					w = ww[i];
					break;
				}
				if (pq1.top().first > ww[i])
				{
					nowk -= dfsm2(pq1.top().second);
					pq1.pop();
				}
				else
				{
					w = ww[i];
					break;
				}
			}
			fir = false;
			while (!pq2.empty())
			{
				auto r = pq2.top();
				if (r.first < w - d)
				{
					break;
				}
				pq2.pop();
				if (nowo[o[r.second]])
				{
					nowk += dfs2(r.second, w);
				}
			}
			maxw = max(maxw, nowk);
		}
		while (!pq1.empty()) pq1.pop();
		while (!pq2.empty()) pq2.pop();
		printf("Case #%lld: %lld\n", tw + 1, maxw);
	}
	return 0;
}
