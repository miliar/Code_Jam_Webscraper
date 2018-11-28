#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <gmp.h>
#include <gmpxx.h>
#define clr(a) memset(a, 0, sizeof(a))

typedef mpz_class ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

class event
{
public:
	int type;
	int size;
	int time;
	event(int time = 0, int type = 0, int size = 0)
	{
		this->time = time;
		this->type = type;
		this->size = size;
	}
	bool operator < (const event & e) const
	{
		if (time != e.time)
			return time < e.time;
		return type < e.type;
	}
};

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	std::vector<event> events;
	std::vector<pii> stack;
	int _n, m;
	scanf("%d%d", &_n, &m);
	ll n = _n;
	ll real_sum = 0;
	for(int i = 0; i < m; i++)
	{
		int a, b, p;
		scanf("%d%d%d", &a, &b, &p);
		events.push_back(event(a, 0, p));
		events.push_back(event(b, 1, p));
		ll l = b - a;
		real_sum += (l * n - (l * (l-1)) / 2) * p;
		//gmp_printf("add len = %Zd, count = %d\n", l.get_mpz_t(), p);
	}
	std::sort(events.begin(), events.end());
	ll cur_sum = 0;
	for(int i = 0; i < (int) events.size(); i++)
	{
		if (events[i].type == 0)
			stack.push_back(pii(events[i].time, events[i].size));
		else
		{
			int size = events[i].size;
			while(size > 0)
			{
				ll l = events[i].time - stack.back().first;
				int d = std::min(size, stack.back().second);
				stack.back().second -= d;
				size -= d;
				if (stack.back().second == 0)
					stack.pop_back();
				cur_sum += (l * n - (l * (l-1)) / 2) * d;
				//gmp_printf("cheat len = %Zd, count = %d\n", l.get_mpz_t(), d);
			}
		}
	}
	ll ans = real_sum - cur_sum;
	gmp_printf("%Zd\n", ans.get_mpz_t());
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
