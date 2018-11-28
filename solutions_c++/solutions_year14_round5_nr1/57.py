/* by Ashar Fuadi (fushar) */

#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
int N;

ll p, q, r, s;
ll data[1000005];
ll total;

ll way1()
{
	ll res = 0;
	
	int j = 2;
	ll A = data[0];
	ll B = data[1];
	ll C = total-data[0]-data[1];
	
	FOR(i, 1, N-1)
	{
		while (j < N && C > A && B + data[j] <= A)
		{
			B += data[j];
			C -= data[j];
			j++;
		}
		
		if (A >= B && A >= C)
			res = max(res, B+C);
		
		A += data[i];
		B -= data[i];
	}
	return res;
}

ll way2()
{
	ll res = 0;
	
	int j = 1;
	ll A = 0;
	ll B = data[0];
	ll C = total-data[0];
	
	FOR(i, 0, N-1)
	{
		while (j < N && (B < C || B < A))
		{
			B += data[j];
			C -= data[j];
			j++;
		}
		
		if (B >= A && B >= C)
			res = max(res, A+C);
		
		A += data[i];
		B -= data[i];
	}
	return res;
}

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d %lld %lld %lld %lld", &N, &p, &q, &r, &s);
		total = 0;
		REP(i, N)
		{
			data[i] = ((i*p+q) % r + s);
			total += data[i];
		}
		ll res = way1();
		reverse(data, data+N);
		res = max(res, way1());
		res = max(res, way2());
		printf("Case #%d: %.10lf\n", tc+1, (double)res/total);
	}
}
