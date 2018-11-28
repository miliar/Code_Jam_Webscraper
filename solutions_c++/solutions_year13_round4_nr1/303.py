#include <cstdio>
#include <iostream>
#include <map>
#include <set>
using namespace std;

const long long Mod = 1000002013;
map<long long, long long> cur;
map<long long, long long> in;
map<long long, long long> out;
set<long long> all;
int N, M;

int main()
{
	int Tcases;
	scanf("%d", &Tcases);
	for ( int cases( 0); cases < Tcases; cases++)
	{
		scanf("%d %d", &N, &M);

		cur.clear();
		in.clear();
		out.clear();
		all.clear();

		long long paid = 0;
		for ( int i( 0); i < M; i++)
		{
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);

			in[o] += p;
			out[e] += p;
			all.insert( o);
			all.insert( e);

			long long tmp = e - o;
			tmp = N * tmp - ( ( ( tmp - 1) * tmp) >> 1);
			paid += ( tmp % Mod) * p;
			paid %= Mod;
		}
//		printf("%lld\n", paid);

		long long ans = 0;
		for ( set<long long>::iterator leg( all.begin()); leg != all.end(); leg++)
		{
			long long sta = *leg;
			cur[sta] += in[sta];
			for ( map<long long, long long>::reverse_iterator rleg( cur.rbegin()); rleg != cur.rend() && out[sta]; rleg++)
			{
				long long diff = min( out[sta], rleg->second);
				rleg->second -= diff;
				out[sta] -= diff;

				long long tmp = sta - rleg->first;
				tmp = N * tmp - ( ( ( tmp - 1) * tmp) >> 1);
				ans += ( tmp % Mod) * diff;
				ans %= Mod;
//				printf("out %d at %d from %d paid %lld\n", diff, sta, rleg->first, tmp);
			}
		}

		printf("Case #%d: %lld\n", cases+1, ( paid - ans + Mod) % Mod);
	}

	return 0;
}
