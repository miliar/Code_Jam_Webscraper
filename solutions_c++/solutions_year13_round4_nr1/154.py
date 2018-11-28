#include <cassert>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>

using namespace std;


const long long P = 1000002013LL;

struct Delta
{
	Delta() {}
	Delta(int p, long long i, long long o) : place(p), in(i), out(o) {}

	int place;
	long long in;
	long long out;

	bool operator<(const Delta & that) const
	{
		return place < that.place;
	}
};

struct Ticket
{
	Ticket(int s, long long c) : start(s), count(c) {}

	int start;
	long long count;

	bool operator<(const Ticket & that) const
	{
		return start < that.start;
	}
};

inline long long sum(long long n)
{
	return (n * (n + 1) / 2) % P;
}

inline long long cost(int n, int len)
{
	return (P + sum(n) - sum(n - len)) % P;
}

long long solve()
{
	int n, m;
	scanf("%i %i", &n, &m);

	vector<Delta> delta;

	long long expected = 0;

	{
		vector<Delta> tmp;

		for(int i = 0; i < m; i++)
		{
			int o, e, p;
			scanf("%i %i %i", &o, &e, &p);

			tmp.push_back(Delta(o, p, 0));
			tmp.push_back(Delta(e, 0, p));

			expected = (expected + cost(n, e - o) * p) % P;
		}

		std::sort(tmp.begin(), tmp.end());

		for(int i = 0; i < tmp.size(); i++)
			if(delta.size() == 0 || delta[delta.size() - 1].place != tmp[i].place)
				delta.push_back(tmp[i]);
			else
			{
				delta[delta.size() - 1].in += tmp[i].in;
				delta[delta.size() - 1].out += tmp[i].out;
			}
	}


	long long real = 0;

	priority_queue<Ticket> q;
	for(int i = 0; i < delta.size(); i++)
	{
		Delta & d = delta[i];

		if(d.in > 0)
			q.push(Ticket(d.place, d.in));

		for(long long c = d.out; c > 0;)
		{
			assert(q.size() > 0);

			Ticket t = q.top();
			q.pop();

			if(c < t.count)
			{
				real = (real + cost(n, d.place - t.start) * (c % P)) % P;

				q.push(Ticket(t.start, t.count - c));
				break;
			}
			else
			{
				real = (real + cost(n, d.place - t.start) * (t.count % P)) % P;

				c -= t.count;
			}
		}
	}

	return (P + expected - real) % P;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%i\n", &t);

	for(int ti = 1; ti <= t; ti++)
		cout << "Case #" << ti << ": " << solve() << "\n";

	return 0;
}
