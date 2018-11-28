#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
#include <stack>
#include <iostream>

using namespace std;

const long long MOD = 1000002013;

long long n;
long long m;

long long L(long long k)
{
	return (n * k - k * (k - 1) / 2) % MOD;
}

void add(long long &x, long long d)
{
	(x += d) %= MOD;
}

int main()
{
//*
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
//*/
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++, printf("\n"))
	{
		printf("Case #%d: ", t);
		cin >> n >> m;
		long long ans = 0;

		stack < pair < long long, long long > > Q;
		map < long long, long long > I, O;

		for (int i = 0; i < m; i++)
		{
			long long x, y, p;
			cin >> x >> y >> p;
			add(ans, L(y - x) * p);
			add(I[x], p);
			add(O[y], p);
		}
		
		map < long long, long long > :: iterator i, o; 
		
		i = I.begin();
		o = O.begin();
		while (i != I.end() || o != O.end())
		{
			if (i != I.end() && (o == O.end() || i->first <= o->first))
			{
				Q.push(*i);
				++i;
			}
			else
			{
				long long r = o->second;
				while (r)
				{
					long long d = min(Q.top().second, r);
					//cout << " " << o->first - Q.top().first << " " << d << endl;
					add(ans, -L(o->first - Q.top().first) * d);
					Q.top().second -= d;
					r -= d;
					if (Q.top().second == 0)
						Q.pop();
				}
				++o;
			}
		}
		cout << (ans + MOD) % MOD;
	}	
    return 0;
}
