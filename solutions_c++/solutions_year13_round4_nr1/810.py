#define mod 1000002013

#include <stdio.h>

#include <algorithm>
#include <queue>

using namespace std;

typedef pair<int, int> P;

struct compare  
{  
  bool operator()(P const& a, P const& b)  
  {  
	  return a.first > b.first || a.first == b.first && a.second < b.second;  
  }  
};

struct compare2 
{  
  bool operator()(P const& a, P const& b)  
  {  
	  return a.first < b.first;
  }  
};

inline long long price(long long s)
{
	return (s * (s - 1) / 2) % mod;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++)
	{
		long long pans = 0;
		long long ans = 0;
		int n, m;

		priority_queue<P, vector<P>, compare> q;

		scanf("%d %d", &n, &m);
		for (int i = 0; i < m; i++)
		{
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			pans = (pans + p * price(e - o)) % mod;
			q.push(make_pair(o, p));
			q.push(make_pair(e, -p));
		}

		priority_queue<P, vector<P>, compare2> cards;

		while (! q.empty())
		{
			P t = q.top();
			if (t.second > 0)
			{
				cards.push(make_pair(t.first, t.second));
			} else
			{
				int p = -t.second;
				while (p > 0)
				{					
					if (cards.top().second > p)
					{
						ans = (ans + p * price(t.first - cards.top().first)) % mod;
						cards.top().second -= p;
						p = 0;						
					} else
					{
						ans = (ans + cards.top().second * price(t.first - cards.top().first)) % mod;
						p -= cards.top().second;
						cards.pop();
					}
				}
			}
			q.pop();
		}

		/*
		while (! q.empty())
		{
			P t = q.top();
			printf("%d %d\n", t.first, t.second);
			q.pop();
		}
		*/

		printf("Case #%d: %I64d\n", test, (ans - pans + mod) % mod);
	}
	
	return 0;
}